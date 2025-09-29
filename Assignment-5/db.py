from pymongo import MongoClient
from config import MONGO_URI

def get_mongo_connection():
    client = MongoClient(MONGO_URI)
    db = client["test"]
    collection = db["weather_data"]
    return collection