import math
from geopy import distance

from Owner import Owner


class Navigator:
    def __init__(self, longitude: float, latitude: float):
        self.__owner = None

        self.__latitude = latitude
        self.__longitude = longitude

        self.__destination_latitude = None
        self.__destination_longitude = None

        self.__remaining_path = None

    def set_destination(self, longitude: float, latitude: float):
        self.__destination_longitude = longitude
        self.__destination_latitude = latitude

    def set_path(self, path):
        self.__remaining_path = path

    def get_destination(self):
        return self.__destination_longitude, self.__destination_latitude

    def get_location(self):
        return self.__longitude, self.__latitude

    def set_owner(self, owner: Owner):
        self.__owner = owner

    def get_current_target_coordinates(self):
        """Возврашает координаты текущей промежуточной точки назначения из построенного маршрута"""
        lat = self.__remaining_path[0]["latitude"]
        lon = self.__remaining_path[0]["longitude"]

        return lon, lat

    def get_next_target_coordinates(self):
        pass

    def update_location(self, longitude: float, latitude: float):
        self.__latitude = latitude
        self.__longitude = longitude

    def get_navigation_tip(self):
        pass

    @staticmethod
    def compute_direction_angle(current_longitude: float, current_latitude: float,
                                target_longitude: float, target_latitude: float):
        """Вычисляет угол представляющий направления движения от одной точки к другой"""

        delta_lat = target_latitude - current_latitude
        delta_lon = target_longitude - current_longitude
        angle = math.atan2(delta_lat, delta_lon)

        return angle

    @staticmethod
    def compute_distance(current_longitude: float, current_latitude: float,
                         target_longitude: float, target_latitude: float):
        """Вычисляет расстояние между двумя точками в метрах"""

        return distance.geodesic((current_latitude, current_longitude),
                                 (target_latitude, target_longitude)).meters

    def set_next_target(self):
        """Меняем текущую промежуточную точку"""
        self.__remaining_path.pop(0)
