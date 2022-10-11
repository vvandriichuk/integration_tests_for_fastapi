from pymongo import MongoClient


def getDB():
    client = MongoClient()
    return client.get_database("config")
