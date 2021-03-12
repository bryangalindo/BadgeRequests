from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routers import badges, requests


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(badges.router)
app.include_router(requests.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
