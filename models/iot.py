from pydantic import BaseModel, Field
from typing import List

class Location(BaseModel):
    lat: float
    lon: float

class Container(BaseModel):
    id: str
    location: Location
    weight: float
    volume: float
    materials: List[str]
    name: str
