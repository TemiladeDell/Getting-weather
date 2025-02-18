import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city, 
        "appid": api_key, 
        "units": "metric"  
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.json()['message']}")

def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {description.capitalize()}")


API_KEY = "get api key"
city = "Lagos"

try:
    weather_data = get_weather(city, API_KEY)
    display_weather(weather_data)
except Exception as e:
    print(e)
