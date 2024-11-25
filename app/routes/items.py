from fastapi import APIRouter, HTTPException
from app.models.item_model import Item
from app.services.item_service import (
    create_item_in_db,
    get_item_from_db,
    get_all_items_from_db,
    delete_item_from_db,
)

router = APIRouter()


@router.post("/", response_model=Item)
async def create_item(item: Item):
    """
    API endpoint to create a new item.
    """
    created_item = await create_item_in_db(item)
    return created_item


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: str):
    """
    API endpoint to fetch an item by its ID.
    """
    item = await get_item_from_db(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=list[Item])
async def get_all_items():
    """
    API endpoint to fetch all items.
    """
    items = await get_all_items_from_db()
