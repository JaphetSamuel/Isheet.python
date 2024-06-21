from typing import List, Optional

from fastapi import APIRouter, HTTPException,status

from isheet.db.models.intervention import Intervention
from isheet.manager.intervention import (
    create_intervention,
    delete_intervention,
    read_intervention,
    search_interventions,
    update_intervention,
)

app = APIRouter()


@app.post("/", response_model=str)
def create_intervention_endpoint(intervention: Intervention):
    intervention_id = create_intervention(intervention.model_dump())
    return intervention_id


@app.get("/{intervention_id}", response_model=Intervention)
def read_intervention_endpoint(intervention_id: str):
    intervention = read_intervention(intervention_id)
    if intervention:
        return intervention
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Intervention not found")


@app.put("/{intervention_id}", response_model=bool)
def update_intervention_endpoint(intervention_id: str, update_data: Intervention):
    success = update_intervention(intervention_id, update_data.model_dump())
    if success:
        return success
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Intervention not found")


@app.delete("/{intervention_id}", response_model=bool)
def delete_intervention_endpoint(intervention_id: str):
    success = delete_intervention(intervention_id)
    if success:
        return success
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Intervention not found")


@app.get("/", response_model=List[Intervention])
def search_interventions_endpoint(
    technician: Optional[str] = None,
    intervention_type: Optional[str] = None,
):
    criteria = {}
    if technician:
        criteria["technician"] = technician
    if intervention_type:
        criteria["intervention_type"] = intervention_type

    interventions = search_interventions(criteria)
    return interventions
