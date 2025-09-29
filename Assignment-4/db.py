import psycopg2
from config import DB_params

def get_connection():
    conn = psycopg2.connect(**DB_params)
    return conn, conn.cursor()

def create_table(cursor,conn):
    cursor.execute(
        """
         CREATE TABLE IF NOT EXISTS new_weather(
        id SERIAL PRIMARY KEY,
        country CHAR(2),
        city VARCHAR(50),
        weather_main VARCHAR(50),
        weather_description VARCHAR(100),
        temp REAL,
        temp_min REAL,
        temp_max REAL,
        pressure REAL,
        humidity REAL,
        visibility INT,
        wind_speed REAL,
        clouds INT,
        inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
        """
    )
    conn.commit()