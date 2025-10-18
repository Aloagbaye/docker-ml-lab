# config.py (Pydantic v2)
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",          # optional
        case_sensitive=False      # env var names NOT case-sensitive
    )

    app_name: str = Field(default="ML Predictor API")
    log_level: str = Field(default="INFO")   # DEBUG/INFO/WARN/ERROR
    model_slope: float = 3.0
    model_intercept: float = 1.0
    redis_url: str = "redis://redis:6379/0"

settings = Settings()
