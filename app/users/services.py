import datetime

from fastapi import HTTPException
from starlette import status

import external_api
from users import crud
from users.schemas import UserSchemaCreate


def save_user_data(user: UserSchemaCreate, response):
    existing_user = crud.get_user_by_phone_number(user.phone_number)

    if existing_user:
        crud.update_user_by_id(existing_user.id, user)
        response.status_code = status.HTTP_200_OK
        return crud.get_user_by_phone_number(user.phone_number)

    return crud.create_user(user)


def get_user_data(data):
    existing_user = crud.get_user_by_phone_number(data.phone_number)

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User with 'phone_number'='{}' is not found".format(data.phone_number)
        )

    # add country code
    t = datetime.datetime.now()
    country_code = external_api.get_country_code_from_dadata(existing_user.country)
    print('Get country code {}'.format(datetime.datetime.now() - t))

    existing_user.country_code = country_code

    return existing_user


def delete_user_data(data):
    existing_user = crud.get_user_by_phone_number(data.phone_number)

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User with 'phone_number'='{}' is not found".format(data.phone_number)
        )

    crud.delete_user(existing_user)

    return
