from functools import lru_cache

from api.auth.schemas import UserCreate, UserRead, UserUpdate
from api.auth.users import auth_backend, fastapi_users
from api.database import create_db_and_tables
from api.settings import get_settings
from api.transport.handlers.admin import admin_router
from api.transport.handlers.site import site_router
from api.transport.handlers.users_auth import user_auth
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


def _setup_api_routers(
    api: APIRouter,
) -> None:
    api.include_router(site_router, tags=["Pages"])
    api.include_router(user_auth)
    api.include_router(admin_router, tags=["Admin"])


@lru_cache
def make_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.project_name,
        # debug=settings.debug,
    )
    app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
    _setup_api_routers(app.router)  # noqa

    origins = [
        "http://localhost",
        "http://localhost:8000/",
        "http://localhost:8000/auth/login",
        "http://localhost:8000/smm",
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
