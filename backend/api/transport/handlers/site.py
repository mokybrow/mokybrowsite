import json
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request


site_router = APIRouter()


templates = Jinja2Templates(directory="../frontend/templates")


@site_router.get('/')
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@site_router.get('/news')
async def home_page(request: Request):
    return templates.TemplateResponse("news.html", {"request": request})


@site_router.get('/about-us')
async def home_page(request: Request):
    return templates.TemplateResponse("about-us.html", {"request": request})


@site_router.get('/works')
async def home_page(request: Request):
    return templates.TemplateResponse("works.html", {"request": request})


@site_router.get('/career')
async def home_page(request: Request):
    return templates.TemplateResponse("career.html", {"request": request})

@site_router.get('/admin/login')
async def home_page(request: Request):
    return templates.TemplateResponse("smm.html", {"request": request})