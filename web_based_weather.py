#this is a web based version of the weather watcher app from Micorsoft copilot 
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
print("load key: ", API_KEY)

@app.route("/", methods = ["GET", "POST"])

def index():
    weather= None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        #Validate city input
        if not city.isalpha():
            error = "⚠ City name must contain only letters."
        else:
            #Fetch weather data from OpenWeatherMap API
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                response = requests.get(url)
                data = response.json()

                if data.get("cod") != 200:
                    error = data.get("message", "CITY NOT FOUND.")
                else:
                    weather = {
                        "city": data["name"],
                        'description': data["weather"][0]["description"].title(),
                        "temp": round(data["main"]["temp"], 1),
                        "humidity": data["main"]["humidity"],
                        "wind": data["wind"]["speed"], 
                        }
            except requests.exceptions.RequestException:
                error = "Network error. Please check internet connection and try again."

    return render_template("index.html", weather=weather,error=error)

if __name__ == "__main__":
    app.run(debug=True)                   