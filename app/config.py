from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration settings for the application.
    Reads environment variables and provides default values if not set.
    """
    APP_NAME: str = "FastAPI Professional Project"
    MONGO_URI: str = "mongodb://localhost:27017/fastapi_db"
    DEBUG: bool = True

    class Config:
        env_file = ".env"  # Specifies the file for environment variables


# Instantiate settings
settings = Settings()
