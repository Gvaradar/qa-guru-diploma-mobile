from pydantic_settings import BaseSettings
from typing import Optional


class Config(BaseSettings):
    context: str = "local"
    remote_url: str = "http://localhost:4723/wd/hub"
    platform_name: str = "Android"
    platform_version: str = "11.0"
    device_name: str = "Pixel 4"
    app: Optional[str] = None
    app_package: str = "org.wikipedia.alpha"
    app_activity: str = "org.wikipedia.main.MainActivity"
    browserstack_username: Optional[str] = None
    browserstack_access_key: Optional[str] = None
    timeout: int = 10

    class Config:
        env_file = ".env"
        extra = "ignore"


def load_config() -> Config:
    from dotenv import load_dotenv
    import os

    context = os.getenv("CONTEXT", "local")
    if context == "browserstack":
        load_dotenv(".env.browserstack")
    else:
        load_dotenv(".env.local")

    return Config()