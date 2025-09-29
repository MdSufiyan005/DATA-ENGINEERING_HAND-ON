

def insert_weather(cursor, conn,data):
    weather_tuple = (
        data['sys']['country'],
        data['name'],
        data['weather'][0]['main'],
        data['weather'][0]['description'],
        data['main']['temp'],
        data['main']['temp_min'],
        data['main']['temp_max'],
        data['main']['pressure'],
        data['main']['humidity'],
        data['visibility'],
        data['wind']['speed'],
        data['clouds']['all'],
    )
    cursor.execute(
        """
        INSERT INTO new_weather(country,city,weather_main,weather_description,temp,temp_min,temp_max,pressure,humidity,visibility,wind_speed,clouds)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,weather_tuple)
    conn.commit()
    