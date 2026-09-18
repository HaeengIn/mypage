from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from auto_template import setup_templates

from routers.license import license_router
from routers.about import about_router
from routers.adofai import adofai_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = setup_templates(directory="templates")


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


@app.middleware("http")
async def strip_trailing_slash(request: Request, call_next):
    path = request.scope["path"]
    if path != "/" and path.endswith("/"):
        request.scope["path"] = path.rstrip("/")
    response = await call_next(request)
    return response


@app.get("/")
async def index(request: Request):
    title = "NaGNae - Official website of HaeengIn"
    h1 = "NaGNae"
    h3 = "Official website of HaeengIn"

    context = {
        "title": title,
        "h1": h1,
        "h3": h3
    }

    return templates.TemplateResponse(
        request=request,
        context=context,
        name="index.html",
    )


@app.get("/help/dollimpan")
async def dollimpan(request: Request):
    title = "돌림판 - 도움말"
    h1 = title

    context = {
        "title": title,
        "h1": h1,
    }

    return templates.TemplateResponse(
        request=request,
        context=context,
        name="help/dollimpan.html",
    )


@app.get("/robots.txt")
async def robots(request: Request):
    return FileResponse("./robots.txt")


@app.get("/sitemap.xml")
async def sitemap(request: Request):
    return FileResponse("./sitemap.xml")


app.include_router(license_router)
app.include_router(about_router)
app.include_router(adofai_router)
