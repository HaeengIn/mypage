from fastapi import APIRouter, Request
from templates_config import templates
import json

download_installer_router = APIRouter(
    prefix="/download-installer", redirect_slashes=True
)

with open("static/db/data.json", "r") as data:
    json_data = json.load(data)


@download_installer_router.get("")
async def index(request: Request):
    installer_data = json_data["download_installer"]

    title = "Windows installer download"
    h1 = "Windows Installer Download"
    h3 = "for HaeengIn"

    context = {"title": title, "h1": h1, "h3": h3, "items": installer_data}

    return templates.TemplateResponse(
        request=request,
        context=context,
        name="download_installer/index.html",
    )
