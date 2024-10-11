import requests
import html
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT  = "https://www.alphavantage.co"
NEW_ENDPOINT = "https://newsapi.org"
account_sid = ""
auth_token = os.environ.get("AUTH_TOKEN")
# stock_apikey = os.environ.get("STOCK_APIKEY")
# news_apikey = os.environ.get('NEWS_APIKEY')
stock_apikey = ""
news_apikey = ""


params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_apikey,
}

response = requests.get("https://www.alphavantage.co/query", params=params)
response.raise_for_status()
try:
    data = response.json()
except ValueError:
    print("There is a problem")
data = html.unescape(response.json()["Time Series (Daily)"])
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
daybefore_closing_price = float(data_list[1]["4. close"])
report = (yesterday_closing_price - daybefore_closing_price)/daybefore_closing_price * 100
print(report)
up_down = none
if report > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
stock_percent = abs(round(report))
if stock_percent > 5:
    params = {
        "apiKey": news_apikey,
        "qInTitle": COMPANY_NAME,
        "pagesize": 3,

    }

    response = requests.get("https://newsapi.org/v2/top-headlines", params=params)
    response.raise_for_status()
    artivles = response.json()["articles"]

    formatted_articles = [f"{STOCK}: {up_down}{stock_percent}%\n Headline: {article['title']}. \bBrief: {article['description']}" for article in artivles]

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='twilio_number',
            to='your_number'
        )

