import pytest
from fastapi.testclient import TestClient
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings
from database import Base
from main import app

client = TestClient(app)

test_engine = create_engine(
    settings.TEST_DATABASE_URL
)

TestingSessionLocal = sessionmaker(bind=test_engine)


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


app.add_middleware(DBSessionMiddleware, db_url=settings.TEST_DATABASE_URL)

new_user_data = {
    "name": "Галина",
    "surname": "Королёва",
    "patronymic": "Николаевна",
    "phone_number": "7999999010",
    "email": "example@gmail.com",
    "country": "Литва"
}


def test_save_user_data(test_db):
    response = client.post("/save_user_data", json=new_user_data)

    assert response.status_code == 201
    assert response.json()['phone_number'] == new_user_data['phone_number']
    assert response.json()['country'] == new_user_data['country']
    assert response.json()['email'] == new_user_data['email']
    assert response.json()['patronymic'] == new_user_data['patronymic']
    assert response.json()['surname'] == new_user_data['surname']
    assert response.json()['name'] == new_user_data['name']


def test_save_user_data_unprocessable_entity(test_db):
    response = client.post("/save_user_data", json={})

    assert response.status_code == 422


def test_get_user_data(test_db):
    client.post("/save_user_data", json=new_user_data)
    response = client.post("/get_user_data", json={'phone_number': new_user_data['phone_number']})

    assert response.status_code == 200


def test_get_user_data_undefined(test_db):
    response = client.post("/delete_user_data", json={'phone_number': '70000000000'})

    assert response.status_code == 404


def test_delete_user_data(test_db):
    client.post("/save_user_data", json=new_user_data)
    response = client.post("/delete_user_data", json={'phone_number': new_user_data['phone_number']})

    assert response.status_code == 204


def test_delete_user_data_undefined(test_db):
    response = client.post("/delete_user_data", json={'phone_number': new_user_data['phone_number']})

    assert response.status_code == 404
