from fastapi.routing import APIRouter

from isheet.web.api import authentication, echo, interventions, monitoring

api_router = APIRouter()
api_router.include_router(authentication.router, prefix="/auth", tags=["auth"])
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(
    interventions.router, prefix="/interventions", tags=["intervention"],
)
