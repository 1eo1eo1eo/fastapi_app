from fastapi import APIRouter, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy.orm import Mapped

from core.models import db_helper
from .schemas import OperationCreate
from .models import Operation


router = APIRouter(
    prefix="/operation",
    tags=["Operation"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(db_helper.session_getter)):
    try:
        stmt = select(Operation).where(Operation.type == operation_type)
        result = await session.execute(stmt)
        return {
            "status":"success",
            "data":result.mappings().all(),
            "details":None,
        }
    except Exception:
         raise HTTPException(status_code=500, detail={
            "status":"error",
            "data":None,
            "detail":None,
         })


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(db_helper.session_getter)):
    stmt = insert(Operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status":"success"}