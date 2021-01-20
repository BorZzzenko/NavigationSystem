from abc import ABC, abstractmethod


class OwnerStateException(Exception):
    """Исключение при неправильных запросах к Geocoder"""
    pass


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
