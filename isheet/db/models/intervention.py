from typing import Optional
from pydantic import BaseModel


class Intervention(BaseModel):
    """Itervention"""
    _id: Optional[str]
    client_name: str
    address: str
    date: str
    start_time: str
    end_time: str
    technician: str
    intervention_type: str
    software: str
    software_version: str
    problem: str
    actions: str
    results: str
    observations: str
    materials: list[str]
