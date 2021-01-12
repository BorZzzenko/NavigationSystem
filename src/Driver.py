from DijkstraForCar import DijkstraForCar
from MoveByCar import MoveByCar
from Owner import Owner


class Driver(Owner):
    def __init__(self):
        super().__init__()
        self._move_action = MoveByCar()
        self._path_finder = DijkstraForCar()
