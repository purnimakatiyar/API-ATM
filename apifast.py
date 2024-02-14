"""Module providing a function fastapi version."""
from fastapi import FastAPI
from routers import account
from routers import auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(account.router)
