from abc import ABC, abstractmethod


class OwnerObserver(ABC):
    @abstractmethod
    def update(self, owner):
        pass
