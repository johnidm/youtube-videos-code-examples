from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    gupshup_api_key: str
    gupshup_app_name: str
    gupshup_app_id: str
    gupshup_source_number: str = "917834811114"
    gupshup_api_base_url: str = "https://api.gupshup.io"


settings = Settings()
