from BikerFactory import BikerFactory
from DriverFactory import DriverFactory
from Geocoder import Geocoder
from Manager import Manager
from Owner import Owner
from PedestrianFactory import PedestrianFactory


class NavigationSystem:
    """Фасад для всей системы"""
    def __init__(self):
        self.__manager = Manager()
        self.__geocoder = Geocoder()

        self.__factories_dict = {
            "pedestrian": PedestrianFactory(),
            "driver": DriverFactory(),
            "biker": BikerFactory(),
        }

    def __get_owner(self, owner_type: str):
        return self.__factories_dict[owner_type].get_owner()

    def add_owner(self, owner_type: str):
        """Добавить владельца в систему

        :param owner_type: тип нового владельца
        """
        owner = self.__get_owner(owner_type)
        self.__manager.add_owner(owner)

    def remove_owner(self, owner):
        self.__manager.remove_owner(owner)

    def give_order(self, owner: Owner, address: str):
        """Выбирает адрес назначения для устройства"""
        self.__manager.give_order(owner, address)

    def get_free_owners(self):
        return self.__manager.get_free_owners()

    def get_busy_owners(self):
        return self.__manager.get_busy_owners()

    def get_owners(self):
        return self.__manager.get_owners()

    def find_coordinates(self, address: str):
        return self.__geocoder.find_coordinates(address)

    def find_address(self, longitude: float, latitude: float):
        return self.__geocoder.find_address(longitude, latitude)

    @staticmethod
    def get_current_target_point(owner):
        return owner.get_navigator().get_current_target_coordinates()

    @staticmethod
    def get_location(owner: Owner):
        navigator = owner.get_navigator()
        return navigator.get_location()

    @staticmethod
    def get_destination_point(owner: Owner):
        navigator = owner.get_navigator()
        return navigator.get_destination()

    @staticmethod
    def get_current_tip(owner: Owner):
        navigator = owner.get_navigator()
        return navigator.get_navigation_tip()

    @staticmethod
    def get_path(owner: Owner):
        navigator = owner.get_navigator()
        return navigator.get_path()

    def perform_move(self):
        """Запускает движение всех устройств в системе"""
        owners = self.__manager.get_owners()

        for owner in owners:
            owner.perform_move()
