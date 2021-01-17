import Navigator
from OwnerObserver import OwnerObserver
from ReadyState import ReadyState


class Owner:
    """Класс владельца устройства"""

    def __init__(self, start_longitude=83.7813856, start_latitude=53.3448302):
        self._observers = list()
        self._move_action = None
        self._navigator = Navigator.Navigator(start_longitude, start_latitude)
        self._path_finder = None
        self._navigator.set_owner(self)
        self._state = ReadyState(self)

    def get_path_finder(self):
        return self._path_finder

    def get_navigator(self):
        return self._navigator

    def get_move_action(self):
        return self._move_action

    def set_destination(self, latitude: float, longitude: float):
        self._state.set_destination(latitude, longitude)

    def perform_move(self):
        """Движение
        Если есть точка назначения и текущее положение != точке назначения,
        то двигаемся
        """
        self._state.perform_move()

    def change_state(self, state):
        self._state = state

    def attach(self, observer: OwnerObserver):
        self._observers.append(observer)

    def detach(self, observer: OwnerObserver):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

