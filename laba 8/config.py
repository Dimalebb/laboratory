from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    bot_token: str = Field(..., env="BOT_TOKEN")
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    model: str = Field("gpt-3.5-turbo", env="MODEL")

    cache_file: str = Field("data/cache_store/gpt_cache.json", env="CACHE_FILE")
    log_file: str = Field("data/bot.log", env="LOG_FILE")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()