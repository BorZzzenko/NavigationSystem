from AStarForPedestrians import AStarForPedestrians
from MoveByFoot import MoveByFoot
from Owner import Owner


class Pedestrian(Owner):
    def __init__(self):
        super().__init__()
        self._move_action = MoveByFoot()
        self._path_finder = AStarForPedestrians()
