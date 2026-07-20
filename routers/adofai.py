import json

from fastapi import APIRouter, Request
from templates_config import templates

adofai_router = APIRouter(prefix="/adofai", redirect_slashes=True)

with open("static/db/data.json", "r") as f:
    data = json.load(f)
    data = list(data["adofai"].values())


@adofai_router.get("")
async def index(request: Request):
    title = "ADOFAI - NaGNae"
    h1 = "A Dance of Fire and Ice"
    h3 = "HaeengIn의 불과 얼음의 춤 활동"

    context = {
        "title": title,
        "h1": h1,
        "h3": h3,
        "repo_link": "https://github.com/HaeengIn/Adofai-Custom-Creates",
    }

    return templates.TemplateResponse(
        request=request, context=context, name="adofai/index.html"
    )


@adofai_router.get("/custom")
async def custom(request: Request):
    title = "커스텀 레벨 다운로드 - NaGNae"
    h1 = "커스텀 레벨 다운로드"
    h3 = "아래의 모든 레벨들의 저작권은 저(HaeengIn)과 공동작업자에게 있습니다."

    context = {"title": title, "h1": h1, "h3": h3, "items": data}

    return templates.TemplateResponse(
        request=request, context=context, name="adofai/custom.html"
    )
