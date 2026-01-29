import os
import httpx
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_dallas_weather(city: str):
    if not API_KEY:
        return {"error": "OPENWEATHER_API_KEY not set"}

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial",
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    return {
        "city": city,
        "temperature_f": data["main"]["temp"],
        "feels_like_f": data["main"]["feels_like"],
        "condition": data["weather"][0]["description"],
    }


# To run the app, use: uvicorn app:app --reload