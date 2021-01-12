from abc import ABC, abstractmethod

from Navigator import Navigator


class Movable(ABC):
    """Интерфейс движения"""
    @abstractmethod
    def move(self, navigator: Navigator):
        """Движение"""
        pass
