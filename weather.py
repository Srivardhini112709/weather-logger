import requests
import mysql.connector
from datetime import datetime

API_KEY = '8e801ff76677648808449ff0b795373f'  
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',           
    'password': '12345',   
    'database': 'weather_project'
}


def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'main' not in data:
        print("Invalid city name or API error.")
        return None

    return {
        'city': city,
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'],
        'observation_time': datetime.now()
    }


def insert_weather(weather):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    query = """
    INSERT INTO weather_data (city, temperature, humidity, description, observation_time)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        weather['city'],
        weather['temperature'],
        weather['humidity'],
        weather['description'],
        weather['observation_time']
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


city = input("Enter city name: ")
weather_data = fetch_weather(city)
if weather_data:
    print(f"\nWeather in {weather_data['city']}:")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Description: {weather_data['description']}")
    print(f"Logged at: {weather_data['observation_time']}")
    insert_weather(weather_data)
    print("✅ Data stored in MySQL database.")

