from math import cos, sin


class Movable:
    """Интерфейс движения"""

    def __init__(self):
        self._speed = None
        self._min_distance_radius = None

    def move(self, navigator):
        """Движение"""

        # Получаем текущие координаты и координаты следующей точки в маршруте
        location = navigator.get_location()
        next_point = navigator.get_current_target_coordinates()

        # Если расстояние между ними меньше 10 метров,
        # Считаем что достигли этой точки
        distance = navigator.compute_distance(*location, *next_point)
        if distance <= self._min_distance_radius:
            navigator.update_location(*next_point)
            navigator.set_next_target()
            return

        # Вычисляем новые координаты (движемся в сторону точки)
        angle = navigator.compute_direction_radians(*location, *next_point)

        longitude = location[0] + self._speed * cos(angle)
        latitude = location[1] + self._speed * sin(angle)

        navigator.update_location(longitude, latitude)
