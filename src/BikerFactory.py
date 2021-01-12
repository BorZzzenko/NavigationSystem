from Biker import Biker
from OwnerFactory import OwnerFactory


class BikerFactory(OwnerFactory):
    def get_owner(self):
        return Biker()
