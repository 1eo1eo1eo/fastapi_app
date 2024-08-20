from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from core.config import settings
from api import router as api_router
from core.models import db_helper
from core.models.base import Base


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

main_app.include_router(
    api_router,
)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )