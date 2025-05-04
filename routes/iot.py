from fastapi import APIRouter
from models.iot import Container
from services import iot_service

router = APIRouter()

@router.post("/contenedores")
def receive_containers(data: list[Container]):
    iot_service.store_containers([d.dict() for d in data])
    return {"message": f"{len(data)} containers stored successfully."}
