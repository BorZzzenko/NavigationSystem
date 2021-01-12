from Movable import Movable


class MoveByFoot(Movable):
    """Движение пешком"""
    def __init__(self):
        self.__speed = 1

    def move(self, navigator):
        print("Иду пешком(")
        navigator.update_location()

