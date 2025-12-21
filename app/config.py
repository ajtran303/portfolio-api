from pathlib import Path
from pydantic_settings import BaseSettings
from typing import Optional

BASE_DIR = Path(__file__).parent
PROJECTS_DIR = BASE_DIR / "projects_md"

class Settings(BaseSettings):
    ASSETS_BASE_URL: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
