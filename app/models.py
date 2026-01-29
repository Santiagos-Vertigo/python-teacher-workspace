from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature_f: float
    feels_like_f: float
    condition: str
