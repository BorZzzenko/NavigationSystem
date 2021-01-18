from Movable import Movable


class MoveByBike(Movable):
    """Движение на ведосипеде"""
    def __init__(self):
        super().__init__()
        # Примерно 4м за одно движение
        self._speed = 0.00005
        self._min_distance_radius = 5
