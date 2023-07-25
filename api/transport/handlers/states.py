import json

from fastapi import APIRouter

from api.settings import get_settings

states_router = APIRouter()


@states_router.get('/')
async def read_root():
    return {'Hello': 'World'}

