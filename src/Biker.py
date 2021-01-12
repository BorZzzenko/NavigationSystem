from DijkstraForBike import DijkstraForBike
from MoveByBike import MoveByBike
from Owner import Owner


class Biker(Owner):
    def __init__(self):
        super().__init__()
        self._move_action = MoveByBike()
        self._path_finder = DijkstraForBike()

