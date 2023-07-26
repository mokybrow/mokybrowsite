from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import FilePath
from starlette.templating import Jinja2Templates

class Settings(
    BaseSettings,
):
    # project_name: str
    # debug: bool
    # states_path: FilePath
    class Config:
        env_prefix = 'QUICK_SUPPORT_'
        env_file = '.env'
        # allow_mutation = False


@lru_cache
def get_settings() -> Settings:
    return Settings()