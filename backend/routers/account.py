from fastapi import APIRouter
from backend.models.account import Account
from backend.db import db
from bson import ObjectId

router = APIRouter()

@router.post("/accounts")
async def create_account(account: Account):
    result = await db.accounts.insert_one(account.dict())
    return {"id": str(result.inserted_id)}

@router.get("/accounts")
async def list_accounts():
    accounts = await db.accounts.find().to_list(100)
    for acc in accounts:
        acc["_id"] = str(acc["_id"])
    return accounts
