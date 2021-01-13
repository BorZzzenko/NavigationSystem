from geopy import Nominatim

from GeocodingSearch import GeocodingSearch


class GeocodingAPI(GeocodingSearch):
    """Делает запросы геокодирования к API"""
    def __init__(self):
        self.__locator = Nominatim(user_agent="myGeocoder")

    def find_address(self, longitude: float, latitude: float):
        coordinates = str(latitude), str(longitude)
        location = self.__locator.reverse(coordinates)
        address = location.address

        return address

    def find_coordinates(self, address: str):
        location = self.__locator.geocode(address)

        return location.longitude, location.latitude
