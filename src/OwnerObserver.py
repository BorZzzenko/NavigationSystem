from abc import ABC, abstractmethod

import Owner


class OwnerObserver(ABC):
    @abstractmethod
    def update(self, owner: Owner):
        pass
