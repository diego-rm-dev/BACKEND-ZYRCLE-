from pydantic import BaseModel

class RoutePoint(BaseModel):
    id: str
    lat: float
    lon: float
    priority: int
    fill_level: float
    weight: float
