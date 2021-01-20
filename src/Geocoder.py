from GeocodingSearch import GeocodingSearch
from GeocodingAPI import GeocodingAPI


class GeocodingException(Exception):
    """Исключение при неправильных запросах к Geocoder"""
    pass


class Geocoder(GeocodingSearch):
    """Proxy для GeocodingAPI"""

    def __init__(self):
        self.__geocodingAPI = None

    def find_address(self, longitude: float, latitude: float):
        """Получает адрес по заданным координатам

        :param longitude: долгота
        :param latitude: ширина
        :raises GeocodingExeption
        :return: str - адрес по заданным координатам
        """
        # Проверка что координаты находяться в пределах города
        if self.__is_valid_coordinates(longitude, latitude):
            self.__initialize_api()
            return self.__geocodingAPI.find_address(longitude, latitude)
        else:
            raise GeocodingException("Координаты находятся за пределами города")

    def find_coordinates(self, address: str):
        """Возвращает координаты по адресу

        :param address: адрес объекта
        :raises GeocodingExeption
        :return: (longitude, latitude) кортеж с долготой и широтой
        """
        # Проверка что адресс содержит "Россия, Барнаул
        if self.__is_valid_address(address):
            self.__initialize_api()
            return self.__geocodingAPI.find_coordinates(address)
        else:
            raise GeocodingException('Адресс должен содержать: "Россия, Барнаул"')

    def __is_valid_address(self, address: str):
        """Проверка что адресс содержит "Россия, Барнаул

        :param address: адрес объекта
        :return: bool
        """
        address_words = address.lower().replace(",", " ").split(" ")

        cities = ["барнаул", "barnaul"]
        countries = ["russia", "россия"]

        is_contains_city = any(city in address_words for city in cities)
        is_contains_country = any(country in address_words for country in countries)

        if is_contains_city and is_contains_country:
            return True

        return False

    def __is_valid_coordinates(self, longitude: float, latitude: float):
        """Проверка что координаты лежит внутри города

        :param longitude: долгота
        :param latitude: ширина
        :return: bool
        """
        # Границы Барнаула по данным с OpenStreetMap
        latitude_edges = [53.2685, 53.4210]
        longitude_edges = [83.4944, 83.9235]

        return (latitude_edges[0] < latitude < latitude_edges[1] and
                longitude_edges[0] < longitude < longitude_edges[1])

    def __initialize_api(self):
        """Инициализирует GeocodingAPI"""
        if self.__geocodingAPI is None:
            self.__geocodingAPI = GeocodingAPI()
