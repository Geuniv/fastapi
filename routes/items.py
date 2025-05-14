from fastapi import APIRouter

item_router = APIRouter(prefix="/items")

@item_router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@item_router.post("/")
async def create_item(item: dict):
    return {"item": item}