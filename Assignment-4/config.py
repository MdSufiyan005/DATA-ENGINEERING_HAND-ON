import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('WHEATHER_API_KEY')

DB_params = {
    "host":f"{os.getenv('HOST')}",
    "database":"weather_reatail_db",
    "user":f"{os.getenv('POSTGRES_USER')}",
    "password":f"{os.getenv('POSTGRES_PASSWORD')}"
}

cities = [
    {"name":"Delhi"},
    {"name":"Mumbai"},
    {"name":"Pune"},
    {"name":"Lucknow"}
]