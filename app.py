from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from templates_config import templates

from routers.license import license_router
from routers.about import about_router
from routers.adofai import adofai_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.middleware("http")
async def add_link_header(request, call_next):
    response = await call_next(request)
    if request.url.path == "/":
        response.headers["Link"] = (
            '<https://haeengin.com/sitemap.xml>; rel="sitemap", '
            '<https://haeengin.com/openapi.json>; rel="describedby", '
            '<https://haeengin.com/docs>; rel="service-doc"'
        )
    return response


@app.get("/")
async def index(request: Request):
    title = "NaGNae - Official website of HaeengIn"
    h1 = "HaeengIn의 공식 웹 사이트"

    context = {
        "title": title,
        "h1": h1,
    }

    return templates.TemplateResponse(
        request=request, context=context, name="index.html"
    )


@app.get("/help/dollimpan")
async def dollimpan(request: Request):
    title = "돌림판 - 도움말"
    h1 = title

    context = {"title": title, "h1": h1}

    return templates.TemplateResponse(
        request=request, context=context, name="help/dollimpan.html"
    )


app.include_router(license_router)
app.include_router(about_router)
app.include_router(adofai_router)
