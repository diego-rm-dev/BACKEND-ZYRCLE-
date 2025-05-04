from fastapi import APIRouter
from services.residence_service import get_mock_residence_data

router = APIRouter()

@router.get("/{residencia_id}/stats")
def get_residence_stats(residencia_id: str):
    return get_mock_residence_data()
