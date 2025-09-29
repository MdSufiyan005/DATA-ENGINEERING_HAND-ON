import time
from db import get_mongo_connection
from fetch import fetch_weather_data
from injest import insert_weather
from config import cities

def main():
    collection = get_mongo_connection()
    for city in cities:
        weather_data = fetch_weather_data(city['name'])
        insert_weather(collection,weather_data,city)
        time.sleep(10)
    
if __name__=="__main__":
    main()