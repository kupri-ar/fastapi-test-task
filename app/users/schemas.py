import secrets

from pydantic import BaseModel, EmailStr, Field


class UserSchemaBase(BaseModel):
    name: str = Field(
        ..., title="User First Name", max_length=50, regex="[\u0401\u0451\u0410-\u044f- ]"
    )
    surname: str = Field(
        ..., title="User Last Name", max_length=50, regex="[\u0401\u0451\u0410-\u044f- ]"
    )
    patronymic: str = Field(
        None, title="User Patronymic", max_length=50, regex="[\u0401\u0451\u0410-\u044f- ]"
    )
    phone_number: str = Field(
        ..., title="User Phone Number", max_length=11, regex="^7[0-9]+"
    )
    country: str = Field(
        ..., title="User Country", max_length=50, regex="[\u0401\u0451\u0410-\u044f- ]"
    )
    email: EmailStr | None = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Брэндон",
                "surname": "Купер",
                "patronymic": "Иванович",
                "phone_number": "79991112030",
                "country": "Франция",
                "email": "example@gmail.com",
            }
        }



class UserSchemaCreate(UserSchemaBase):
    user_id: str = Field(
        secrets.token_hex(16)[:12], title="User Identify", max_length=12
    )


class UserSchema(UserSchemaBase):
    country_code: int = Field(
        None, title="User Country Code"
    )

    class Config:
        orm_mode = True


class UserRequestBody(BaseModel):
    phone_number: str = Field(
        ..., title="User Phone Number", max_length=11, regex="^7[0-9]+"
    )

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "79991112030"
            }
        }
