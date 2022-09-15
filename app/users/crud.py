from fastapi_sqlalchemy import db

from users.models import User
from users.schemas import UserSchemaCreate, UserSchema


def create_user(user: UserSchemaCreate):
    db_user = User(**user.dict())
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user


def get_user_by_phone_number(phone_number: str):
    return db.session.query(User).where(User.phone_number == phone_number).first()


def update_user_by_id(id_: int, user: UserSchemaCreate):
    db.session.query(User).where(User.id == id_).update(user.dict(exclude={'user_id'}))
    db.session.commit()
    return


def delete_user(user: UserSchema):
    db.session.delete(user)
    db.session.commit()
    return
