from fastapi import APIRouter
from fastapi import Depends

from auth.base_config import current_user
from .tasks import send_email_report_dashboard


router = APIRouter(
    prefix="/report",
    tags=["Tasks"]
)


@router.get("/dashboard")
async def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return {
        "status":200,
        "data":"Message sent",
        "details":None,
    }