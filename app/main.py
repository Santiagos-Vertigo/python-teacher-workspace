from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from app.weather_fast import get_dallas_weather
from app.models import WeatherResponse

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_model=dict)
def root():
    return {"message": "Dallas Weather API is running"}

@app.get("/weather", response_model=WeatherResponse)
def weather(city: str = Query("Dallas")):
    return get_dallas_weather(city)