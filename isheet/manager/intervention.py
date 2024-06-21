# Fonction pour créer une intervention
from typing import List, Optional

from bson import ObjectId

from isheet.db import db
from isheet.db.models.intervention import Intervention

interventions_collection = db.get_collection("interventions")


def create_intervention(intervention_data: dict) -> str:
    """ create  new intervetion"""
    intervention = Intervention(**intervention_data)
    result = interventions_collection.insert_one(intervention.dict())
    return str(result.inserted_id)



def read_intervention(intervention_id: str) -> Optional[Intervention]:
    """ read intervention"""
    result = interventions_collection.find_one({"_id": ObjectId(intervention_id)})
    if result:
        return Intervention(**result)
    return None


# Fonction pour mettre à jour une intervention par id
def update_intervention(intervention_id: str, update_data: dict) -> bool:
    """ update intervention"""
    result = interventions_collection.update_one(
        {"_id": ObjectId(intervention_id)},
        {"$set": update_data},
    )
    return result.modified_count > 0


# Fonction pour supprimer une intervention par id
def delete_intervention(intervention_id: str) -> bool:
    """delete intervention"""
    result = interventions_collection.delete_one({"_id": ObjectId(intervention_id)})
    return result.deleted_count > 0


# Fonction pour rechercher des interventions par un critère
def search_interventions(criteria: dict) -> List[Intervention]:
    """search intervention"""
    results = interventions_collection.find(criteria)
    return [Intervention(**intervention) for intervention in results]
