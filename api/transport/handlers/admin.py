from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse

from fastapi.templating import Jinja2Templates
from fastapi_mail import FastMail, MessageSchema, MessageType

from api.auth.users import current_active_user, current_superuser

from api.auth.database import User
from api.email.send_email import EmailSchema, conf



admin_router = APIRouter()


templates = Jinja2Templates(directory="frontend/templates")


@admin_router.get("/admin/login")
async def home_page(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})


@admin_router.get("/admin/dashboard")
async def authenticated_route(request: Request, user: User = Depends(current_superuser)):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request, 'message': user.email})
    #return {"message": f"Hello {user.email}!"}


@admin_router.get("/mail")
async def send_in_background(
    email: EmailSchema
    ) -> JSONResponse:
    html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.get("email"),
        template_body=email.get("email"),
        subtype=MessageType.html,
        )
    print(message.template_body)
    fm = FastMail(conf)

    await fm.send_message(message, template_name='email.html')

    return JSONResponse(status_code=200, content={"message": "email has been sent"})