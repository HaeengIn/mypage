from fastapi import APIRouter, Request, HTTPException
from templates_config import templates

license_router = APIRouter(prefix="/license", redirect_slashes=True)

@license_router.get("")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="license/index.html")

@license_router.get("/wppengine")
async def wppengine(request: Request):
    return templates.TemplateResponse(request=request, name="license/wppengine/index.html")

@license_router.get("/")

@license_router.get("/wppengine/shiro")
async def wppengine_pages(request: Request):
    from supabase_client import supabase
    return templates.TemplateResponse(request=request, name="license/wppengine/shiro.html")