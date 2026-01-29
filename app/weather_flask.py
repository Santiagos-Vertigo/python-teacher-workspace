from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY = "25c4ba952ec792a2f8c313550be9ed86"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    params = {
        "q": city,
        "appid": API_KEY, 
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# To run the app, use: flask run