from Owner import Owner


class Navigator:
    def __init__(self, longitude: float, latitude: float):
        self.__owner = None

        self.__latitude = latitude
        self.__longitude = longitude

        self.__destination_latitude = None
        self.__destination_longitude = None

        self.__remaining_path = None

    def set_destination(self, longitude: float, latitude: float):
        self.__destination_longitude = longitude
        self.__destination_latitude = latitude

    def get_destination(self):
        return self.__destination_longitude, self.__destination_latitude

    def get_location(self):
        return self.__longitude, self.__latitude

    def set_owner(self, owner: Owner):
        self.__owner = owner

    def get_current_target_coordinates(self):
        pass

    def get_next_target_coordinates(self):
        pass

    def update_location(self):
        pass

    def get_navigation_tip(self):
        pass

    def compute_angle(self, current_latitude: float, current_longitude: float,
                      target_latitude: float, target_longitude: float):
        pass

    def compute_distance(self, current_latitude: float, current_longitude: float,
                         target_latitude: float, target_longitude: float):
        pass
