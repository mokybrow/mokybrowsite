from fastapi import APIRouter, Request
from api.auth.database import User
from fastapi import Depends, FastAPI
from api.auth.users import fastapi_users, auth_backend
from api.auth.users import fastapi_users, current_active_user


user_router = APIRouter(fastapi_users.get_auth_router(auth_backend))
