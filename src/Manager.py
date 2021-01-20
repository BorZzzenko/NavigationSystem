from Geocoder import Geocoder
from Owner import Owner
from OwnerObserver import OwnerObserver


class Manager(OwnerObserver):
    """Класс Менеджера - выдает устройства, выбирает адреса назначения"""

    def __init__(self):
        self.__busy_owners = list()
        self.__free_owners = list()
        self.__geocoder = Geocoder()

    def get_owners(self):
        return self.__free_owners + self.__busy_owners

    def get_free_owners(self):
        return self.__free_owners

    def get_busy_owners(self):
        return self.__busy_owners

    def add_owner(self, owner: Owner):
        self.__free_owners.append(owner)
        owner.attach(self)

    def remove_owner(self, owner: Owner):
        if owner in self.__free_owners:
            self.__free_owners.remove(owner)
            owner.detach(self)
        elif owner in self.__busy_owners:
            self.__busy_owners.remove(owner)
            owner.detach(self)

    def give_order(self, owner: Owner, address: str):
        """Выбирает адрес назначения для владельца навигатора"""

        # Находит координаты по адресу
        longitude, latitude = self.__geocoder.find_coordinates(address)

        # Устанавливает точку назначения
        owner.set_destination(longitude, latitude)

        # Добавляет в список занятых
        self.__busy_owners.append(owner)
        if owner in self.__free_owners:
            self.__free_owners.remove(owner)

    def update(self, owner: Owner):
        if owner in self.__busy_owners:
            self.__busy_owners.remove(owner)
            self.__free_owners.append(owner)
