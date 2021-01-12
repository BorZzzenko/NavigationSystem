from abc import ABC, abstractmethod


class OwnerFactory(ABC):
    """Интерфейс фабрика владельцев устройст"""
    @abstractmethod
    def get_owner(self):
        pass
