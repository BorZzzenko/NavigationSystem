from Movable import Movable


class MoveByFoot(Movable):
    """Движение пешком"""

    def __init__(self):
        super().__init__()
        self._speed = 0.000001
        self._min_distance_radius = 5

