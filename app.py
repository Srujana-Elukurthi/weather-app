from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.environ.get("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("Please set the WEATHER_API_KEY environment variable.")

@app.route('/')
def get_weather():
    # Get city from query parameter; default is 'London'
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city name in the URL, e.g., ?city=London"}), 400

    # Call OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    # Handle invalid city or API errors
    if response.status_code != 200:
        return jsonify({"error": f"Could not fetch weather for '{city}'. Please check the city name."}), 400

    data_json = response.json()

    # Prepare response data
    data = {
        "city": city.title(),
        "temperature": f"{data_json['main']['temp']}°C",
        "weather": data_json['weather'][0]['description'].title(),
        "humidity": f"{data_json['main']['humidity']}%",
        "wind": f"{data_json['wind']['speed']} km/h"
    }

    return jsonify(data)

if __name__ == "__main__":
    # Flask app runs on port 5000 inside container
    app.run(host="0.0.0.0", port=5000)


