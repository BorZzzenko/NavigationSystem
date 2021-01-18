from Movable import Movable


class MoveByFoot(Movable):
    """Движение пешком"""

    def __init__(self):
        super().__init__()
        # Примерно 2м за одно движение
        self._speed = 0.000025
        self._min_distance_radius = 5

