import os

from fastapi.templating import Jinja2Templates
from starlette.requests import Request


def canonical_url_processor(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {"canonical_url": f"{base_url}{request.url.path}"}


templates = Jinja2Templates(
    directory="templates",
    context_processors=[canonical_url_processor],
)


def static_version(path):
    return os.path.getmtime(path)


templates.env.globals["static_version"] = static_version
