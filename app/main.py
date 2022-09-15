from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from config import settings
from users import models
from database import engine
from users.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Fast API Test Task'
)

app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)

app.include_router(router)
