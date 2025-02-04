import requests
import json

# OpenWeather API Details
API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "your_actual_api_key_here"  # Replace with your OpenWeather API key

# Set location (e.g., London)
params = {"q": "London", "appid": API_KEY}

# Fetch data from OpenWeather API
response = requests.get(API_URL, params=params)

# Check if API request was successful
if response.status_code == 200:
    data = response.json()

    # Save the response data into a file
    with open("data/raw/weather.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Data saved successfully!")

else:
    print(f"❌ Error fetching data: {response.status_code} - {response.text}")
