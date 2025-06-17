from fastapi import APIRouter
from backend.db import db
import httpx

router = APIRouter()

@router.get("/import-products")
async def import_products():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fakestoreapi.com/products")
        products = response.json()

        # Opcional: evitar duplicados
        for product in products:
            existing = await db.products.find_one({"id": product["id"]})
            if not existing:
                await db.products.insert_one(product)

    return {"message": f"{len(products)} productos importados"}
@router.get("/products")
async def get_products():
    products = await db.products.find().to_list(100)
    for p in products:
        p["_id"] = str(p["_id"])
    return products
