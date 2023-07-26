import json
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request


site_router = APIRouter()


templates = Jinja2Templates(directory="api/templates")


@site_router.get('/')
async def home_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
