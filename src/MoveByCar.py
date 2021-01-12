from Movable import Movable


class MoveByCar(Movable):
    """Движение на машине"""
    def __init__(self):
        self.__speed = 1

    def move(self, navigator):
        print("Еду на машине")
        navigator.update_location()
