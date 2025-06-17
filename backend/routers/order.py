from fastapi import APIRouter
from backend.models.order import Order
from backend.db import db
from bson import ObjectId

router = APIRouter()

@router.post("/orders")
async def create_order(order: Order):
    result = await db.orders.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@router.get("/orders")
async def list_orders():
    orders = await db.orders.find().to_list(100)
    for order in orders:
        order["_id"] = str(order["_id"])
    return orders
