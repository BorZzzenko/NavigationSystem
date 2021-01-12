from abc import ABC, abstractmethod


class GeocodingSearch(ABC):
    """Интерфейс геокодирования"""
    @abstractmethod
    def find_address(self, longitude: float, latitude: float):
        """Получает адрес по заданным координатам

        :param longitude: долгота
        :param latitude: ширина
        :return: str - адрес по заданным координатам
        """

        pass

    @abstractmethod
    def find_coordinates(self, address: str):
        """Возвращает координаты по адресу

        :param address: адрес объекта
        :return: (longitude, latitude) кортеж с долготой и широтой
        """

        pass
