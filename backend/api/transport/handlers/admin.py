
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from api.auth.users import auth_backend, current_active_user, fastapi_users, current_superuser

from api.auth.database import User

admin_router = APIRouter()


templates = Jinja2Templates(directory="../frontend/templates")


@admin_router.get("/admin/login")
async def home_page(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})


@admin_router.get("/admin/dashboard")
async def authenticated_route(request: Request, user: User = Depends(current_superuser)):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request, 'message': user.email})
    return {"message": f"Hello {user.email}!"}