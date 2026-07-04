from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.dashboard import DashboardResponse
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"],
)


# ==========================================================
# GET DASHBOARD
# ==========================================================

@router.get(
    "",
    response_model=DashboardResponse,
)
def get_dashboard(
    db: Session = Depends(get_db),
):
    return DashboardService.get_dashboard(
        db,
    )