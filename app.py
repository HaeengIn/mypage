from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from templates_config import templates

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
    return templates.TemplateResponse(request=request, name="index.html")
