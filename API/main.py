import json
from typing import Optional

from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import requests as req
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.config import Config

from Data.connection import Table
from dependencies import get_current_user
from Routers import badges, requests, applications, auth, users
from notify import prepare_bot_message, send_chat_notification


app = FastAPI()
api = FastAPI()

# Submounted the API + routers because mounting the client to "/" ignores all subpaths
app.mount("/api/v1", api)
app.mount("/", StaticFiles(directory="Client/public", html=True), name="client")
app.mount("/build", StaticFiles(directory="Client/public/build"), name="build")

# Removed .env to allow the package to read computer environment variables
config = Config()

CONF_URL="https://accounts.google.com/.well-known/openid-configuration"
HOST_HTTP_URL = config('HOST_HTTP_URL', cast=str)
HOST_HTTPS_URL = config('HOST_HTTPS_URL', cast=str)
GOOGLE_CHAT_WEBHOOK_URL = config('GOOGLE_CHAT_WEBHOOK_URL', cast=str)

origins = [
    HOST_HTTP_URL,
    HOST_HTTPS_URL,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key='!secret')

api.include_router(badges.router)
api.include_router(requests.router)
api.include_router(applications.router)
api.include_router(auth.router)
api.include_router(users.router)

oauth = OAuth(config)

oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@app.get("/")
async def root():
    return RedirectResponse(url='client')


@api.get('/login', tags=['auth'])
async def login(request: Request):
    # Redirect Google OAuth back to our application
    redirect_uri = request.url_for('auth')
    
    return await oauth.google.authorize_redirect(request, redirect_uri)


@api.route('/auth')
async def auth(request: Request):
    # Perform Google OAuth
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)

    # Save the user
    request.session['user'] = dict(user)
    
    return RedirectResponse(url=HOST_HTTPS_URL)


# Tag it as "authentication" for our docs
@api.get('/logout', tags=['auth'])
async def logout(request: Request):
    # Remove the user
    request.session.pop('user', None)

    return RedirectResponse(url=HOST_HTTPS_URL)


@api.post('/notify', tags=['notify'])
async def notify(request: Request):
    submitted_application_json = await request.json()
    message = prepare_bot_message(submitted_application_json)
    send_chat_notification(message, GOOGLE_CHAT_WEBHOOK_URL, HOST_HTTPS_URL)
