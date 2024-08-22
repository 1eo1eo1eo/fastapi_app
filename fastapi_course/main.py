from fastapi_users import FastAPIUsers, fastapi_users
from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from src.core.config import settings
from src.core.models import db_helper
from src.auth.base_config import auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.auth.models import User
from src.auth.manager import get_user_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
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


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )