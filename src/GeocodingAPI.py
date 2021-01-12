from GeocodingSearch import GeocodingSearch

class GeocodingAPI(GeocodingSearch):
    """Делает запросы геокодирования к API"""

    def find_address(self, longitude: float, latitude: float):
        return "Россия, Барнаул, пр. Северный Власихинский 64"

    def find_coordinates(self, address: str):
        return 83.51, 53.25
