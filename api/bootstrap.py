from functools import lru_cache

from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from api.settings import get_settings
from api.transport.handlers.site import site_router


def _setup_api_routers(
    api: APIRouter,
) -> None:
    api.include_router(site_router, tags=["Pages"])


@lru_cache
def make_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.project_name,
        # debug=settings.debug,
    )
    app.mount("/static", StaticFiles(directory="api/static"), name="static")
    _setup_api_routers(app.router)  # noqa
    return app