from amadeus import Client, ResponseError
from datetime import datetime
import requests



# "https://test.api.amadeus.com/v2/shopping/flight-offers?" \
# "originLocationCode=SYD&destinationLocationCode=BKK&departureDate=2024-11-02&adults=1&nonStop=false&max=5"


AMADEUS_CLIENT_ID = "LyWCfKrf8fGU2CNgPp4Wov4CB8zWF1vf"
AMADEUS_CLIENT_SECRET = "6ge2OehUUE2TCod0"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

params = {
    "originLocationCode": "PAR",
    "destinationLocationCode": "BKK",
    "departureDate": "2024-011-02",
    "maxPrice": "400",
    "adults": 1,
    "nonStop": "false",
    "max": 5,
}



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = AMADEUS_CLIENT_ID
        self.api_secret = AMADEUS_CLIENT_SECRET
        self.data = {}
        self.access_token = self.get_new_token()

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=AMADEUS_ENDPOINT, data=body, headers=header)
        response.raise_for_status()
        return response.json()['access_token']

    def get_data(self):
        response = requests.get(AMADEUS_ENDPOINT, json=params, headers=headers)
        response.raise_for_status()
        self.data = response.json()
        return response.status_code

    def get_destination_code(self, city_name):
        print(f"Using this token to get destination {self.access_token}")
        headers = {"Authorization": f"Bearer {self.access_token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code