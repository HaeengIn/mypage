import json

from fastapi import APIRouter, Request
from templates_config import templates

about_router = APIRouter(prefix="/about", redirect_slashes=True)


@about_router.get("")
async def index(request: Request):
    with open("static/db/data.json", "r") as f:
        data = json.load(f)
        data = data["about"].values()

        title = "About - NaGNae"
        h1 = "Introducing HaeengIn"
        h3 = """ADOFAI Amatuer Charter
        FastAPI & Python Developer"""

        context = {
            "title": title,
            "h1": h1,
            "h3": h3,
            "items": data,
        }

        return templates.TemplateResponse(
            request=request, context=context, name="about.html"
        )
