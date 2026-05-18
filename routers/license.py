from fastapi import APIRouter, Request, HTTPException
from templates_config import templates
from typing import Any, cast

license_router = APIRouter(prefix="/license", redirect_slashes=True)


@license_router.get("")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="license/index.html")


@license_router.get("/wallpaperengine")
async def wallpaperengine(request: Request):
    return templates.TemplateResponse(
        request=request, name="license/wallpaperengine/index.html"
    )


@license_router.get("/wallpaperengine/shiro")
async def shiro(request: Request):
    from supabase_client import supabase

    try:
        response = (
            supabase.table("wallpaperengine_verification")
            .select("*")
            .eq("target", "shiro")
            .order("name", desc=False)
            .execute()
        )
        rows = response.data

        return templates.TemplateResponse(
            request=request,
            context={"verifications": rows},
            name="license/wallpaperengine/base.html",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@license_router.get("/wallpaperengine/hello2026")
async def hello2026(request: Request):
    screenshot_url = "https://oydyuozovkyalcqshmdr.supabase.co/storage/v1/object/public/verification_screenshot/wallpaperengine/hello2026/Hello(BPM)2026.avif"
    return templates.TemplateResponse(
        request=request,
        context={"screenshot_url": screenshot_url},
        name="license/wallpaperengine/hello2026.html",
    )
