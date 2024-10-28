from dotenv import load_dotenv
import os
import requests
from pprint import pprint

def get_curr_weather(city="mansehra"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    get_curr_weather()