from .trades import router as trades_router
from .users import router as users_router

from fastapi import APIRouter
from core.config import settings

router = APIRouter(
    prefix=settings.api.prefix
)

routers = users_router, trades_router

for rtr in routers:
    router.include_router(rtr)