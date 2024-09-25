import requests
from datetime import datetime

NUTRITION_PASSWORD = "SOCnutr1x%"

NUTRIX_ID = "77b25680"
NUTRIX_KEY = "e377caf1798d85dcebffcf1806c0e04e"
NUTRIX_ENDPOINT = "http://trackapi.nutritionix.com"
SHETTY_ENDPOINT = "https://api.sheety.co/feee438b476315d063792bc36fccdd9a/workoutTracking/workouts"

###################### Format the workout data using NUTRIX API ######################
exercise_endpoint = f"{NUTRIX_ENDPOINT}/v2/natural/exercise"
header_params = {
    "x-app-id": NUTRIX_ID,
    "x-app-key": NUTRIX_KEY,
    "Content-Type": "application/json",
}
data = input("What exercises did you did today?")
exercise_params = {
    "query": data,
    "gender": "male",
    "weight_kg": 128,
    "height_cm": 183,
    "age": 27,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=header_params)
response.raise_for_status()
workout_data = response.json()


###################### Connection with the sheet API ######################
# username OvidiuSuciu
# parola P@ssw0rd


# get data records from the sheet
# response = requests.get(url=SHETTY_ENDPOINT)
# response.raise_for_status()
# print(response.json())

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in workout_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHETTY_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)

#No Authentication
sheet_response = requests.post(SHETTY_ENDPOINT, json=sheet_inputs)

#Basic Authentication
sheet_response = requests.post(
  SHETTY_ENDPOINT,
  json=sheet_inputs,
  auth=(
      "OvidiuSuciu",
      "P@ssw0rd",
  )
)
YOUR_TOKEN = "T3ZpZGl1U3VjaXU6UEBzc3cwcmQ="
#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {YOUR_TOKEN}"
}
sheet_response = requests.post(
    SHETTY_ENDPOINT,
    json=sheet_inputs,
    headers=bearer_headers
)
