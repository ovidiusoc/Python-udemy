from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


flight_search_ex = FlightSearch()
status = flight_search_ex.get_data()

print(status)
print(flight_search_ex.data)