from fastapi import FastAPI
import uvicorn
from app.routes import items
from app.utils.logger import setup_logger
from app.db.connection import connect_to_mongo, close_mongo_connection
from app.config import settings

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Professional Project",
    description="A modular and scalable FastAPI project with MongoDB.",
    version="1.0.0",
)

# Set up logger
logger = setup_logger()


@app.on_event("startup")
async def on_startup():
    """
    Tasks to execute during application startup:
    - Connect to MongoDB.
    - Log the startup event.
    """
    logger.info("Starting FastAPI application...")
    await connect_to_mongo()
    logger.info("MongoDB connection established.")


@app.on_event("shutdown")
async def on_shutdown():
    """
    Tasks to execute during application shutdown:
    - Disconnect from MongoDB.
    """
    logger.info("Shutting down FastAPI application...")
    await close_mongo_connection()
    logger.info("MongoDB connection closed.")


# Include API routes
app.include_router(items.router, prefix="/api/items", tags=["Items"])


@app.get("/", tags=["Health Check"])
async def health_check():
    """
    Health Check endpoint.
    """
    return {"status": "Healthy", "message": "FastAPI application is running!"}


if __name__ == "__main__":
    """
    Programmatic entry point for running the application.
    """
    uvicorn.run(
        "app.main:app",  # Path to FastAPI app instance
        host="127.0.0.1",  # Localhost
        port=8000,  # Port number
        reload=True  # Auto-reload during development
    )
