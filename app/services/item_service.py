from bson.objectid import ObjectId
from app.db.connection import mongo_client
from app.models.item_model import Item

# Reference the MongoDB collection
collection = mongo_client["fastapi_db"]["items"]


async def create_item_in_db(item: Item) -> dict:
    """
    Creates a new item in the MongoDB database.
    """
    result = await collection.insert_one(item.dict(by_alias=True))
    return {**item.dict(), "_id": str(result.inserted_id)}


async def get_item_from_db(item_id: str) -> dict:
    """
    Retrieves a single item from the database by its ID.
    """
    if not ObjectId.is_valid(item_id):
        return None
    item = await collection.find_one({"_id": ObjectId(item_id)})
    return item


async def get_all_items_from_db() -> list:
    """
    Retrieves all items from the MongoDB database.
    """
    items = await collection.find().to_list(100)
    return items


async def delete_item_from_db(item_id: str) -> bool:
    """
    Deletes an item from the MongoDB database by its ID.
    """
    if not ObjectId.is_valid(item_id):
        return False
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0
