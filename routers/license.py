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
    try:
        response = (supabase.table("shiro_verification").select("*").execute())
        rows = response.data

        status_map = {0: "Disallowed", 1: "Allowed", 2: "Partially Allowed"}
        for row in rows:
            row["verify_status_text"] = status_map.get(row["verify_status"], "Unknown") #type: ignore
        
        return templates.TemplateResponse(request=request, context={"verifications": rows}, name="license/wppengine/shiro.html")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))