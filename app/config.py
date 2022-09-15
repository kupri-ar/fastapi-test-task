from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Test Task"
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    DADATA_TOKEN: str

    class Config:
        env_file = "../.env"


settings = Settings()
