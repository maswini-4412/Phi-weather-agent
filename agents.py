from phi.agent import Agent
import requests
import os

from dotenv import load_dotenv
load_dotenv()


# ---------- Agent 1: Weather Agent ----------
class WeatherAgent(Agent):
    def run(self, city: str):
        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }


# ---------- Agent 2: Content Agent ----------
class ContentAgent(Agent):
    def run(self, weather_data: dict):
        paragraph = (
            f"The current weather in {weather_data['city']} is {weather_data['description']}. "
            f"The temperature is {weather_data['temperature']}°C with a humidity level of "
            f"{weather_data['humidity']}%. Overall, the weather conditions are moderate."
        )
        return paragraph
