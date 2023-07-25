from functools import lru_cache

from fastapi import APIRouter, FastAPI

from api.settings import get_settings
from api.transport.handlers.states import states_router


def _setup_api_routers(
    api: APIRouter,
) -> None:
    api.include_router(states_router, prefix='/states')


@lru_cache
def make_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        # title=settings.project_name,
        # debug=settings.debug,
    )
    _setup_api_routers(app.router)  # noqa
    return app