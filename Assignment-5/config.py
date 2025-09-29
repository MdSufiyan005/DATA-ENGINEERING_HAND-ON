import dotenv,os
from dotenv import load_dotenv
load_dotenv()

weather_api_key = os.getenv("WHEATHER_API_KEY")

MONGO_URI=os.getenv("MONGO_URI")

cities = [
    {"name":"Delhi"},
    {"name":"Mumbai"},
    {"name":"Pune"},
    {"name":"Lucknow"}
    # {"name":"Banglore"},
    # {"name":"Hydrabad"},
]