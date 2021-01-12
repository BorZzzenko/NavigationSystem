from abc import ABC, abstractmethod


class PathFinder(ABC):
    @abstractmethod
    def find_path(self, start_longitude: float, start_latitude: float,
                  destination_longitude: float, destination_latitude: float):
        pass
