import requests
from datetime import datetime
import html
import time
from twilio.rest import Client


API_KEY = ""
MY_LAT = 46.770920
MY_LON = 23.589920
account_sid = ""
auth_token = ""


def get_the_weather():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "cnt": 4,
        "appid": API_KEY,
        }
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = html.unescape(response.json())

    for item in data["list"]:
        weather = item["weather"][0]["id"]
        if weather < 700:
            return True
    return False


is_raining = get_the_weather()
if is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Take an umbrella, it will rain today",
        from_='twilio_number',
        to='your_number'
    )
    print(message.status)

