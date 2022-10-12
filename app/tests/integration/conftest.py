import pytest

from pymongo import MongoClient
from fastapi.testclient import TestClient

from app.main import app
from app.db.db import getDB


def override_get_db():
    client = MongoClient()
    try:
        db = client.get_database("test_db")
        yield db
    finally:
        client.close()


def reset_database(db):
    """Clear database after each test."""
    for name in db.list_collection_names():
        collection = db.get_collection(name)
        collection.delete_many({})


@pytest.fixture(scope="session")
def database():
    return MongoClient().get_database("test_db")


@pytest.fixture(scope="session")
def testClient(database):
    with TestClient(app) as client:
        app.dependency_overrides[getDB] = override_get_db
        yield client
        reset_database(database)
        app.dependency_overrides = {}
