from Driver import Driver
from OwnerFactory import OwnerFactory


class DriverFactory(OwnerFactory):
    def get_owner(self):
        return Driver()
