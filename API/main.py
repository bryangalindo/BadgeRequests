import json
from typing import Optional

from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests as req
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.config import Config

from Data.connection import Table
from dependencies import get_current_user
from Routers import badges, requests, applications, auth


app = FastAPI()
config = Config()

CONF_URL="https://accounts.google.com/.well-known/openid-configuration"
CLIENT_HOST_URL = config('CLIENT_HOST_URL', cast=str)
GOOGLE_CHAT_WEBHOOK_URL = config('GOOGLE_CHAT_WEBHOOK_URL', cast=str)

origins = [
    CLIENT_HOST_URL,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key='!secret')

app.include_router(badges.router)
app.include_router(requests.router)
app.include_router(applications.router)
app.include_router(auth.router)

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
    return {"message": "Hello World"}


@app.get('/login', tags=['auth'])
async def login(request: Request):
    # Redirect Google OAuth back to our application
    redirect_uri = request.url_for('auth')
    
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.route('/auth')
async def auth(request: Request):
    # Perform Google OAuth
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)

    # Save the user
    request.session['user'] = dict(user)
    
    return RedirectResponse(url=CLIENT_HOST_URL)


# Tag it as "authentication" for our docs
@app.get('/logout', tags=['auth'])
async def logout(request: Request):
    # Remove the user
    request.session.pop('user', None)

    return RedirectResponse(url=CLIENT_HOST_URL)


@app.post('/notify', tags=['notify'])
async def notify(request: Request):
    badge_app_json = await request.json()
    
    email = badge_app_json['PartitionKey']
    badge_requests_list = '\n- '.join([badge['title'] for badge in badge_app_json['requests']])
    message = f'Incoming badge application!\n\n*User*: {email}\n*Badges*:\n- {badge_requests_list}'
    
    bot_message = {
        'text' : message
    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    try:
        response = req.post(url=GOOGLE_CHAT_WEBHOOK_URL,
            headers=message_headers,
            data=json.dumps(bot_message),
        )
        return RedirectResponse(url=CLIENT_HOST_URL)
    except Exception as e:
        print(e)
    