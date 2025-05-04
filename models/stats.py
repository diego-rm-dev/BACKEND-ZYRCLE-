from pydantic import BaseModel
from typing import Dict, List

class CollectionStats(BaseModel):
    today: Dict[str, float]
    week: Dict[str, float]
    carbon_monthly: Dict[str, float]

class ContainerDetail(BaseModel):
    name: str
    status: str
    fill_level: float
    weight: float
    tokens: float
    co2_saved: float

class ResidenceStats(BaseModel):
    name: str
    total_containers: int
    total_weight: float
    cycle_tokens: float
    carbon_offset: float
    activity_by_material: Dict[str, Dict[str, Dict[str, float]]]
    containers: List[ContainerDetail]
