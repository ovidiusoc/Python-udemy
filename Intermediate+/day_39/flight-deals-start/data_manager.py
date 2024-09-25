import requests

SHETTY_ENDPOINT = "https://api.sheety.co/feee438b476315d063792bc36fccdd9a/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.value = 0

    def update_data(self, sheet_inputs):
        response = requests.post(SHETTY_ENDPOINT, json=sheet_inputs)
