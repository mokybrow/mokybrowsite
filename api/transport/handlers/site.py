import json

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

site_router = APIRouter()


templates = Jinja2Templates(directory="frontend/templates")


@site_router.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@site_router.get("/news")
async def news_page(request: Request):
    return templates.TemplateResponse("news.html", {"request": request})


@site_router.get("/about-us")
async def about_us_page(request: Request):
    return templates.TemplateResponse("about-us.html", {"request": request})


@site_router.get("/works")
async def works_page(request: Request):
    return templates.TemplateResponse("works.html", {"request": request})


@site_router.get("/career")
async def career_page(request: Request):
    return templates.TemplateResponse("career.html", {"request": request})

