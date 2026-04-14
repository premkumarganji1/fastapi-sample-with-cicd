# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Production App"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
