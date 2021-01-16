from math import cos, sin

from Movable import Movable


class MoveByCar(Movable):
    """Движение на машине"""
    def __init__(self):
        self.__speed = 0.0001

    def move(self, navigator):
        # Получаем текущие координаты и координаты следующей точки в маршруте
        location = navigator.get_location()
        next_point = navigator.get_current_target_coordinates()

        # Если расстояние между ними меньше 10 метров,
        # Считаем что достигли этой точки
        distance = navigator.compute_distance(*location, *next_point)
        if distance <= 10:
            navigator.update_location(*next_point)
            navigator.set_next_target()
            return

        # Вычисляем новые координаты (движемся в сторону точки)
        angle = navigator.compute_direction_angle(*location, *next_point)

        longitude = location[0] + self.__speed * cos(angle)
        latitude = location[1] + self.__speed * sin(angle)

        navigator.update_location(longitude, latitude)
