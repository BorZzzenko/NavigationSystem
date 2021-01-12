from OwnerFactory import OwnerFactory
from Pedestrian import Pedestrian


class PedestrianFactory(OwnerFactory):

    def get_owner(self):
        return Pedestrian()
