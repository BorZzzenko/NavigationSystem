from OwnerState import OwnerState
import ReadyState


class MoveState(OwnerState):
    def __init__(self, owner):
        super().__init__(owner)

    def set_destination(self, longitude: float, latitude: float):
        pass

    def perform_move(self):
        navigator = self._owner.get_navigator()

        # Совершаем одно движение
        move_action = self._owner.get_move_action()
        move_action.move(navigator)

        location = navigator.get_location()
        destination = navigator.get_destination()

        # Проверяем достигли ли точки назначения
        if location == destination:
            # Изменяем состояние
            self._owner.change_state(ReadyState.ReadyState(self._owner))
            # Уведомляем менеджера
            self._owner.notify()
