# with open("weather_data.csv") as data_file:
#     data = data_file.readline()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)
# print(type(data["temp"]))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data['temp'].mean())
# max_temp = data['temp'].max()
# # get data from rows
# row = data[data.day == 'Monday']
# monday_temp = row.temp[0]
# value = (monday_temp * 9 / 5) + 32
# print(value)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("nex_data.csv")
print(data)