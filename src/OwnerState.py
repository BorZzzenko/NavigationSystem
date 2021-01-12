from abc import ABC, abstractmethod


class OwnerState(ABC):
    def __init__(self, owner):
        self._owner = owner

    @abstractmethod
    def set_destination(self, latitude: float, longitude: float):
        pass

    @abstractmethod
    def prepare_for_move(self):
        pass

    @abstractmethod
    def perform_move(self):
        pass
