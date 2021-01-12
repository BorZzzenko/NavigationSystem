from MoveState import MoveState
from OwnerState import OwnerState


class ReadyState(OwnerState):
    def set_destination(self, latitude: float, longitude: float):
        pass

    def prepare_for_move(self):
        print("Теперь есть цель")

        device = self._owner.get_device()

        destination = device.get_destination()
        location = device.get_location()

        path_finder = self._owner.get_path_finder()
        path = path_finder.find_path(*location, *destination)

        self._owner.get_navigator().make_tips(path)

        self._owner.change_state(MoveState(self._owner))

    def perform_move(self):
        print("У меня нет цели, а значит и нет пути")
