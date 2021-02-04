import math

from geopy import distance


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

    def get_path(self):
        return self.__remaining_path

    def set_owner(self, owner):
        self.__owner = owner

    def get_current_target_coordinates(self):
        """Возврашает координаты текущей промежуточной точки назначения из построенного маршрута"""
        if self.__remaining_path:
            lat = self.__remaining_path[0]["latitude"]
            lon = self.__remaining_path[0]["longitude"]

            return lon, lat

        return None

    def get_next_target_coordinates(self):
        """Возврашает координаты следующей промежуточной точки назначения из построенного маршрута"""
        if self.__remaining_path and len(self.__remaining_path) > 1:
            lat = self.__remaining_path[1]["latitude"]
            lon = self.__remaining_path[1]["longitude"]

            return lon, lat

        return None

    def update_location(self, longitude: float, latitude: float):
        self.__latitude = latitude
        self.__longitude = longitude

    def get_navigation_tip(self):
        """Возвращает подсказку следования по маршруту"""

        # Берем текущую промежуточную точку маршрута и следующую
        current_target = self.get_current_target_coordinates()
        next_target = self.get_next_target_coordinates()

        if next_target is not None:
            # Определяем текущее направление движения и следующее направление движения
            current_direction = self.compute_direction_clockwise(self.__longitude, self.__latitude, *current_target)
            next_direction = self.compute_direction_clockwise(*current_target, *next_target)

            direction_delta = round(current_direction) - round(next_direction)

            if 10 < direction_delta < 170 or -350 < direction_delta < -190:
                direction_tip = "Поверните направо через"
            elif -170 < direction_delta < -10 or 190 < direction_delta < 350:
                direction_tip = "Поверните налево через"
            else:
                direction_tip = "Продолжайте движение еще"
        elif current_target is not None:
            direction_tip = "Продолжайте движение еще"
        else:
            return "Точка назначения не задана"

        # Вычисляем расстояние до текущей промежуточной
        distance = self.compute_distance(self.__longitude, self.__latitude, *current_target)
        distance = round(distance)

        # Формируем подсказку
        tip = f"{direction_tip} {distance}м"

        return tip

    @staticmethod
    def compute_direction_clockwise(longitude, latitude, target_longitude, target_latitude):
        """Возвращает направление движения между от одной точки к другой - от 0 до 359

        :return: угол от 0 до 359
        """
        angle = math.degrees(math.atan2(math.sin(target_longitude - longitude) * math.cos(target_latitude),
                                          math.cos(latitude) * math.sin(target_latitude) -
                                          math.sin(latitude) * math.cos(target_latitude) *
                                          math.cos(target_longitude - longitude)))

        # Если было -90, теперь 270
        # Если было -179, теперь 181
        if float(angle) < 0:
            angle = 360 - abs(angle)

        return angle

    @staticmethod
    def compute_direction_radians(current_longitude: float, current_latitude: float,
                                  target_longitude: float, target_latitude: float):
        """Вычисляет угол представляющий направление движения от одной точки к другой"""

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
