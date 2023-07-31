from functools import lru_cache
from typing import Any

from fastapi import APIRouter, Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from api.auth.database import User

from api.database import create_db_and_tables
from api.auth.schemas import UserCreate, UserRead, UserUpdate

from api.settings import get_settings
from api.auth.users import auth_backend, fastapi_users
from api.auth.users import current_active_user



user_auth = APIRouter()

user_auth.include_router(
        fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["auth"]
    )
user_auth.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )
user_auth.include_router(
        fastapi_users.get_reset_password_router(),
        prefix="/auth",
        tags=["auth"],
    )
user_auth.include_router(
        fastapi_users.get_verify_router(UserRead),
        prefix="/auth",
        tags=["auth"],
    )
user_auth.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
        prefix="/users",
        tags=["users"],
    )


@user_auth.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@user_auth.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()


