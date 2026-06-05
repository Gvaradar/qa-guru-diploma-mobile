import os
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


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


def load_config() -> Config:
    # Сначала определяем контекст из переменной окружения
    context = os.getenv("CONTEXT", "local")

    # Загружаем соответствующий .env файл
    if context == "browserstack":
        load_dotenv(".env.browserstack", override=True)
    else:
        load_dotenv(".env.local", override=True)

    # Перечитываем контекст после загрузки .env
    final_context = os.getenv("CONTEXT", context)

    return Config(
        context=final_context,
        remote_url=os.getenv("remote_url", "http://localhost:4723/wd/hub"),
        platform_name=os.getenv("platform_name", "Android"),
        platform_version=os.getenv("platform_version", "11.0"),
        device_name=os.getenv("device_name", "Pixel 4"),
        app=os.getenv("app"),
        app_package=os.getenv("app_package", "org.wikipedia.alpha"),
        app_activity=os.getenv("app_activity", "org.wikipedia.main.MainActivity"),
        browserstack_username=os.getenv("browserstack_username"),
        browserstack_access_key=os.getenv("browserstack_access_key"),
        timeout=int(os.getenv("timeout", "10"))
    )
