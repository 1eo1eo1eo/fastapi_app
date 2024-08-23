from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


# class ApiPrefix(BaseModel):
#     prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class Auth(BaseModel):
    secret_key: str

class SMTP(BaseModel):
    user: str
    password: str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template",".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__"
    )
    run: RunConfig = RunConfig()
   # api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig
    auth: Auth
    smtp: SMTP

settings = Settings() # type: ignore