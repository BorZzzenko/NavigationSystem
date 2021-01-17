from Movable import Movable


class MoveByBike(Movable):
    """Движение на ведосипеде"""
    def __init__(self):
        super().__init__()
        self._speed = 0.00001
        self._min_distance_radius = 5
