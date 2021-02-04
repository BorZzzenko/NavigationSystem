from Movable import Movable


class MoveByCar(Movable):
    """Движение на машине"""
    def __init__(self):
        super().__init__()
        # Примерно 10м за одно движение
        self._speed = 0.0001
        self._min_distance_radius = 10
