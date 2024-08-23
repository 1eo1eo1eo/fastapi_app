from fastapi_users import FastAPIUsers, fastapi_users
from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis


from core.config import settings
from core.models import db_helper
from auth.base_config import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.models import User
from auth.manager import get_user_manager
from operations.router import router as router_operation


@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    #shutdown
    await db_helper.dispose()


main_app = FastAPI(
    title="Trading App",
    lifespan=lifespan,
)

fastapi_users = FastAPIUsers[User, int]( #type: ignore
    get_user_manager,
    [auth_backend],
)

main_app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

main_app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

main_app.include_router(
    router_operation,

)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )