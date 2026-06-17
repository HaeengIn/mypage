from fastapi import APIRouter, Request, HTTPException
from templates_config import templates

license_router = APIRouter(prefix="/license", redirect_slashes=True)


@license_router.get("")
async def index(request: Request):
    title = "허가 증명 스크린샷 - NaGNae"
    return templates.TemplateResponse(
        request=request, context={"title": title}, name="license/index.html"
    )


@license_router.get("/wallpaperengine")
async def wallpaperengine(request: Request):
    title = "허가 증명 스크린샷 [Wallpaper Engine] - NaGNae"
    return templates.TemplateResponse(
        request=request,
        context={"title": title},
        name="license/wallpaperengine/index.html",
    )


@license_router.get("/wallpaperengine/{page}")
async def wallpaperengine_page(request: Request, page: str):
    from supabase_client import supabase

    pages = ["shiro", "hello2026"]
    title_map = {"shiro": "SHIRO", "hello2026": "Hello (BPM) 2026"}
    title = f"Wallpaper Engine - {title_map[page]}"

    if page in pages:
        try:
            response = (
                supabase.table("wallpaperengine_verification")
                .select("*")
                .eq("target", page)
                .order("name", desc=False)
                .execute()
            )
            data = response.data

            return templates.TemplateResponse(
                request=request,
                context={"items": data, "title": title},
                name="license/wallpaperengine/base.html",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="Page not found")
