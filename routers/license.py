from fastapi import APIRouter, Request, HTTPException

from auto_template import setup_templates

license_router = APIRouter(prefix="/license")

templates = setup_templates(directory="templates")


@license_router.get("")
async def index(request: Request):
    title = "허가 증명 스크린샷 - NaGNae"
    h1 = "허가 증명 스크린샷"

    context = {"title": title, "h1": h1}

    return templates.TemplateResponse(
        request=request, context=context, name="license/index.html"
    )


@license_router.get("/wallpaperengine")
async def wallpaperengine(request: Request):
    title = "허가 증명 스크린샷 [Wallpaper Engine] - NaGNae"
    h1 = "월 페이퍼 엔진"
    h3 = "Wallpaper Engine"

    context = {"title": title, "h1": h1, "h3": h3}

    return templates.TemplateResponse(
        request=request,
        context=context,
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
