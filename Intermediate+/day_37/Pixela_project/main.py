import requests
from datetime import datetime

USERNAME = "ovibiu"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPHID,
    "name": "KG graph",
    "unit": "kilogram",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": "anj4w4nana4",
}


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"

today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much do you weight today?"),
}
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
# pixel_value_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

# # response = requests.delete(url=pixel_value_endpoint, headers=headers)
# print(response.text)
# response = requests.put(url=pixel_value_endpoint, json={"quantity": "128.6"}, headers=headers)
# print(response.text)

