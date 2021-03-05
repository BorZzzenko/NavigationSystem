from MoveState import MoveState
from OwnerState import OwnerState, OwnerStateException


class ReadyState(OwnerState):
    def set_destination(self, longitude: float, latitude: float):
        # Устанавливаем точку назначения
        navigator = self._owner.get_navigator()
        navigator.set_destination(longitude, latitude)

        location = navigator.get_location()

        # Находим маршрут
        path_finder = self._owner.get_path_finder()
        path = path_finder.find_path(*location, longitude, latitude)

        navigator.set_path(path)

        # Изменяем состояние
        self._owner.change_state(MoveState(self._owner))

    def perform_move(self):
        raise OwnerStateException("Нельзя двигаться без заданной точки назначения...")
