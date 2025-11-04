from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

def connect_to_db():
    client = MongoClient(os.getenv("MONGO_URI"))
    return client["hospital_db"]