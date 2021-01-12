from OwnerState import OwnerState
import ReadyState


class MoveState(OwnerState):
    def __init__(self, owner):
        super().__init__(owner)

    def set_destination(self, latitude: float, longitude: float):
        pass

    def prepare_for_move(self):
        print("У меня уже есть цель")

    def perform_move(self):
        device = self._owner.get_device()

        move_action = self._owner.get_move_action()
        move_action.move(device)

        location = device.get_location()
        destination = device.get_destination()
        notifier = self._owner.get_notifier()

        if notifier is not None:
            notifier.get_notification(*location, 500)

        if location == destination:
            print("Я завершил свой путь")
            self._owner.change_state(ReadyState.ReadyState(self._owner))
            self._owner.notify()
