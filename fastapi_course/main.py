from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis


from core.config import settings
from core.models import db_helper
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from operations.router import router as router_operation
from tasks.router import router as router_tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    redis = aioredis.from_url(f"redis://{settings.redis.host}:{settings.redis.port}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    #shutdown
    await db_helper.dispose()


main_app = FastAPI(
    title="Trading App",
    lifespan=lifespan,
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

main_app.include_router(
    router_tasks,
)



if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )