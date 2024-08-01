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
        return None

def display_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error fetching weather data!")

def weather_app():
    api_key = "your_api_key_here"
    city = input("Enter the city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    weather_app()
