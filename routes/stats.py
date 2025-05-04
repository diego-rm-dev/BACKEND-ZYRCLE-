from fastapi import APIRouter
from services import iot_service, stats_service

router = APIRouter()

@router.get("/coleccion")
def collection_stats():
    data = iot_service.get_all_containers()
    return stats_service.mock_stats(data)
