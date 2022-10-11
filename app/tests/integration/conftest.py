import pytest

from pymongo import MongoClient
from fastapi.testclient import TestClient

from app.main import app
from app.db.db import getDB


def override_get_db():
    client = MongoClient("mongodb://localhost:27017/")
    try:
        db = client.get_database("test_db")
        yield db
    finally:
        client.close()


@pytest.fixture(scope="session")
def database():
    return MongoClient("mongodb://localhost:27017/").get_database("test_db")


def _resetDatabase(db):
    for name in db.list_collection_names():
        collection = db.get_collection(name)
        collection.delete_many({})


@pytest.fixture(scope="session")
def testClient(database):
    with TestClient(app) as client:
        app.dependency_overrides[getDB] = override_get_db
        yield client
        _resetDatabase(database)
        app.dependency_overrides = {}
