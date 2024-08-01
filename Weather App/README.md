# Weather App

This is a simple Weather App written in Python that fetches and displays weather data for a given location using the OpenWeatherMap API.

Features:
- Fetch current weather data for a specified city
- Display weather information such as temperature, weather description, humidity, and wind speed

How to Use:
1. Clone the Repository:
   Clone this repository to your local machine using:
   git clone <repository_url>

2. Navigate to the Project Directory:
   cd <repository_directory>

3. Install Required Libraries:
   Install the required libraries using pip:
   pip install requests

4. Get an API Key:
   Sign up at OpenWeatherMap (https://openweathermap.org/api) to get your API key.

5. Run the Application:
   Execute the `weather_app.py` file to start the application:
   python weather_app.py

6. Enter City Name:
   - You will be prompted to enter the name of a city.
   - The application will fetch and display the current weather data for the specified city.

Code Explanation:
Functions:
- get_weather(city, api_key): Fetches weather data for the specified city using the OpenWeatherMap API.
- display_weather(weather_data): Displays the fetched weather data.

Example:
Here's an example of how the application works:

Enter the city name: Toronto
Weather in Toronto:
Temperature: 22.5°C
Weather: Clear sky
Humidity: 60%
Wind Speed: 5.1 m/s

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements:
- Inspired by various basic Python weather app examples.
- Created as a learning project to understand Python APIs, HTTP requests, and JSON parsing.
