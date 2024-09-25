import requests
import html
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# command with exported env variables:
# export APP_API_KEY=value; export AUTH_TOKEN= value; python3 main.py

MY_LAT = 46.770920
MY_LON = 23.589920
account_sid = ""
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("APP_API_KEY")

def get_the_weather():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "cnt": 4,
        "appid": api_key,
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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Take an umbrella, it will rain today",
        from_='twilio_number',
        to='your_number'
    )
    print(message.status)

