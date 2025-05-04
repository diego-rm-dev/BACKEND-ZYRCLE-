from fastapi import APIRouter
from pydantic import BaseModel
from math import sqrt
from typing import List
from services.gemini import optimize_route_with_gemini


router = APIRouter()

class Location(BaseModel):
    latitude: float
    longitude: float

# Mock data quemada (ahora una sola lista que comparten ambos endpoints)
class Container(BaseModel):
    id: int
    address: str
    type: str
    estimatedWeight: float
    fillPercentage: int
    status: str
    lastUpdated: str
    latitude: float
    longitude: float

# Contenedores actualizados con nuevas ubicaciones y datos
containers_db = [
    Container(
        id=1,
        address="Calle 10 #43B-30, Medellín",
        type="Plástico",
        estimatedWeight=7.2,
        fillPercentage=55,
        status="Medio",
        lastUpdated="2025-04-24T15:10:00Z",
        latitude=6.209520,
        longitude=-75.567820,
    ),
    Container(
        id=2,
        address="Carrera 48 #32B-20, Medellín",
        type="Vidrio",
        estimatedWeight=4.1,
        fillPercentage=25,
        status="Disponible",
        lastUpdated="2025-04-24T14:40:00Z",
        latitude=6.244830,
        longitude=-75.573640,
    ),
    Container(
        id=3,
        address="Calle 33 #76-120, Medellín",
        type="Orgánico",
        estimatedWeight=9.8,
        fillPercentage=92,
        status="Lleno",
        lastUpdated="2025-04-24T13:20:00Z",
        latitude=6.243670,
        longitude=-75.601230,
    ),
    Container(
        id=4,
        address="Carrera 43F #16A Sur-80, Medellín",
        type="Metales",
        estimatedWeight=6.3,
        fillPercentage=47,
        status="Medio",
        lastUpdated="2025-04-24T12:55:00Z",
        latitude=6.173960,
        longitude=-75.605700,
    ),
]


@router.get("/rutas/quemadas", response_model=List[Container])
def get_mock_route():
    # Usamos el mismo array de contenedores para este endpoint
    return containers_db

@router.post("/rutas/optimizar", response_model=List[Container])
def optimize_route(user_location: Location):
    user_location_dict = user_location.dict()
    optimized_ids = optimize_route_with_gemini(containers_db, user_location_dict)
    
    # Crear un diccionario para acceso rápido
    container_map = {c.id: c for c in containers_db}
    
    # Filtrar y devolver los contenedores en el orden sugerido
    ordered = [container_map[cid] for cid in optimized_ids if cid in container_map]
    
    return ordered
