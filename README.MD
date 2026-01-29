# Dallas Weather API

A simple FastAPI backend service that returns current weather data using the OpenWeatherMap API.

## Features
- FastAPI with automatic OpenAPI docs
- GET /weather endpoint
- Query parameter support for city name
- Environment-based API key configuration
- Typed responses using Pydantic

## Tech Stack
- Python 3.11+
- FastAPI
- Uvicorn
- Requests
- Pydantic
- python-dotenv

## Setup

### 1. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
``` 
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Set up environment variables
Create a `.env` file in the project root with the following content:
```
OPENWEATHER_API_KEY=your_real_key_here
```
Replace `your_real_key_here` with your actual OpenWeatherMap API key.
### 4. Run the application
```bash
uvicorn app.weather_flask:app --reload
```
### 5. Access the API
Open your browser and navigate to `http://localhost:8000/docs` to view the interactive API documentation.
## Usage
To get the current weather for a city, send a GET request to:
```http://localhost:8000/weather?city=CityName
``` Replace `CityName` with the desired city.
## Example Response
```json
{
  "city": "Dallas",
  "temperature": 30.5,
  "description": "clear sky",
  "humidity": 40
}
``` 
## License
This project is licensed under the MIT License.
