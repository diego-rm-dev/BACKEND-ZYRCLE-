from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status_check():
    return {"mensaje": "Backend reciclando verde 🌱"}
