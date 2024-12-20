from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvironmentVariables(BaseSettings):
    verify_token: str
    app_secret: str
    facebook_access_token: str

    openai_api_key: str
    tavily_api_key: str

    model_config = SettingsConfigDict(env_file=".env")


env = EnvironmentVariables()