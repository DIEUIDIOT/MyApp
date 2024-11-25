from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

mongo_client: AsyncIOMotorClient = None


async def connect_to_mongo():
    """
    Establish a connection to MongoDB.
    """
    global mongo_client
    try:
        mongo_client = AsyncIOMotorClient(settings.MONGO_URI)
        print(f"Connected to MongoDB at {settings.MONGO_URI}")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise


async def close_mongo_connection():
    """
    Close the MongoDB connection.
    """
    global mongo_client
    if mongo_client:
        mongo_client.close()
        print("MongoDB connection closed.")
