from fastapi import APIRouter
from backend.models.user import User
from backend.db import db
from bson import ObjectId

router = APIRouter()

@router.post("/users")
async def create_user(user: User):
    result = await db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

@router.get("/users")
async def list_users():
    users = await db.users.find().to_list(100)
    for user in users:
        user["_id"] = str(user["_id"])
    return users
