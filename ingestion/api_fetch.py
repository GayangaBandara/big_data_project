import requests
import json

API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "your_api_key"

params = {"q": "London", "appid": API_KEY}
response = requests.get(API_URL, params=params)
data = response.json()

with open("../data/raw/weather.json", "w") as f:
    json.dump(data, f)

print("Data saved successfully!")
