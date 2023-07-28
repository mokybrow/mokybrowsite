from functools import lru_cache


from pydantic import FilePath, BaseSettings
from starlette.templating import Jinja2Templates




class Settings(
    BaseSettings,
):
    project_name: str = "Mishka Studio"
    # project_name: str
    # debug: bool
    # states_path: FilePath
    #database_url = os.environ.get('DATABASE_URL')    
    class Config:
        env_prefix = 'QUICK_SUPPORT_'
        env_file = '.env'
        # allow_mutation = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
