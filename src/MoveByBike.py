from Movable import Movable


class MoveByBike(Movable):
    """Движение на ведосипеде"""
    def __init__(self):
        self.__speed = 1

    def move(self, navigator):
        print("Еду на велике")
        navigator.update_location()
