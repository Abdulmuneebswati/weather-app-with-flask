from flask import Flask , render_template ,request
from weather import get_curr_weather
from waitress import serve
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.html",
    )

@app.route("/weather")
def weather():

    city = request.args.get("city")
    print(bool(city.strip()))
    if not bool(city.strip()):
        city = "mansehra"
    weather_data = get_curr_weather(city)

    if not weather_data["cod"] == 200:
        return render_template("city-not-found.html")
    

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"],
        feels_like= weather_data["main"]["feels_like"],
        temp= weather_data["main"]["temp"]
    )

if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=8000)