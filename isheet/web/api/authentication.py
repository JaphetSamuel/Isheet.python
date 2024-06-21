from fastapi import APIRouter

from isheet import db
from isheet.db.models.authentication import User
from isheet.services.authentication.utils import get_password_hash

router = APIRouter()


@router.post("/users", response_model=User)
async def create_user(user: User):
    user_data = user.model_dump()
    user_data["password"] = get_password_hash(user.password)
    db.users.insert_one(user_data)
    return user
