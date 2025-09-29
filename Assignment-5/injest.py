
def insert_weather(collection, weather_data, city):
    # Check if API returned valid weather
    if weather_data.get("cod") != 200:
        print(f"Skipping insert: API returned error for {city} -> {weather_data.get('message')}")
        return
    
    # Add a custom timestamp field
    weather_data["inserted_at"] = weather_data.get("dt", None)
    
    collection.insert_one(weather_data)
    print(f"Inserted weather data for {city}")