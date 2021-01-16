from abc import ABC, abstractmethod


class OwnerState(ABC):
    def __init__(self, owner):
        self._owner = owner

    @abstractmethod
    def set_destination(self, longitude: float, latitude: float):
        """Установить точку назначения"""
        pass

    @abstractmethod
    def perform_move(self):
        """Совершить движение"""
        pass
