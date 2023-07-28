from functools import lru_cache

from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from api.database import create_db_and_tables
from api.auth.schemas import UserCreate, UserRead, UserUpdate

from api.settings import get_settings
from api.transport.handlers.site import site_router
from api.transport.handlers.users_auth import user_router
from api.auth.users import auth_backend, fastapi_users


def _setup_api_routers(
    api: APIRouter,
) -> None:
    api.include_router(site_router, tags=["Pages"])

    api.include_router(user_router, prefix="/auth/jwt", tags=["auth"]
    )

    # api.include_router(
    #     fastapi_users.get_register_router(UserRead, UserCreate),
    #     prefix="/auth",
    #     tags=["auth"],
    # )
    # api.include_router(
    #     fastapi_users.get_reset_password_router(),
    #     prefix="/auth",
    #     tags=["auth"],
    # )
    # api.include_router(
    #     fastapi_users.get_verify_router(UserRead),
    #     prefix="/auth",
    #     tags=["auth"],
    # )
    # api.include_router(
    #     fastapi_users.get_users_router(UserRead, UserUpdate),
    #     prefix="/users",
    #     tags=["users"],
    # )


@lru_cache
def make_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.project_name,
        # debug=settings.debug,
    )
    app.mount("/static", StaticFiles(directory="api/static"), name="static")
    _setup_api_routers(app.router)  # noqa

    @app.on_event("startup")
    async def on_startup():
        await create_db_and_tables()

    return app
