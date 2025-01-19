from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from app.main import app as fastapi_app

app = FastAPI()

# Add FastAPI as WSGI middleware
app.mount("/", WSGIMiddleware(fastapi_app))
