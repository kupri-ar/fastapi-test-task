from fastapi import APIRouter, Response, Body
from starlette import status

from users import services
from users.schemas import UserSchemaCreate, UserSchema, UserRequestBody

router = APIRouter()


@router.post(
    "/save_user_data",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
    responses={200: {"model": UserSchema}},
    tags=["Users"]
)
def save_user_data(user: UserSchemaCreate, response: Response):
    """
    Create a user or update existing user.
    """

    user_data = services.save_user_data(user, response)

    return user_data


@router.post(
    "/get_user_data",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
    tags=["Users"]
)
def get_user_data(data: UserRequestBody):
    """
    Get a user by phone number.
    """

    user_data = services.get_user_data(data)

    return user_data


@router.post(
    "/delete_user_data",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Users"]
)
def delete_user_data(data: UserRequestBody):
    """
    Delete a user by phone number.
    """

    services.delete_user_data(data)

    return
