import requests
from t39_40flight_data import FlightData

class FlightSearch:

    def get_destination_code(self, city_name):
        # Yahan asli API call ki jagah temporary code return karwa do
        code = "PAR" if city_name == "Paris" else "TEST"
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        # Testing ke liye ek fake flight data return karwa do taaki email notification check ho sake
        if destination_city_code == "PAR":
            flight_data = FlightData(
                price=150,  # Yeh price lowestPrice se kam honi chahiye taaki email chali jaye
                origin_city="London",
                origin_airport="LON",
                destination_city="Paris",
                destination_airport="PAR",
                out_date="2026-09-01",
                return_date="2026-09-08"
            )
            return flight_data
        return None