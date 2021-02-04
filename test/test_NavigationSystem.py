import unittest
from unittest import mock

from Biker import Biker
from Driver import Driver
from NavigationSystem import NavigationSystem
from OwnerState import OwnerStateException
from Pedestrian import Pedestrian


class NavigationSystemTest(unittest.TestCase):
    @mock.patch("osmnx.graph_from_place")
    def test_adding_owners(self, mock):
        system = NavigationSystem()

        system.add_owner("biker")
        system.add_owner("pedestrian")
        system.add_owner("driver")

        owners = system.get_free_owners()

        self.assertEqual(len(owners), 3)

        self.assertIsInstance(owners[0], Biker)
        self.assertIsInstance(owners[1], Pedestrian)
        self.assertIsInstance(owners[2], Driver)

    @mock.patch("osmnx.graph_from_place")
    @mock.patch("Geocoder.Geocoder.find_coordinates", return_value=(1, 1))
    @mock.patch("Owner.Owner.set_destination")
    def test_give_order_to_free_owner(self, get_graph, find_coordinates, set_destination):
        system = NavigationSystem()
        system.add_owner("biker")
        owner = system.get_free_owners()[0]

        system.give_order(owner, "address")

        free_owners = system.get_free_owners()
        busy_owners = system.get_busy_owners()

        self.assertEqual(len(free_owners), 0)
        self.assertEqual(len(busy_owners), 1)

    @mock.patch("osmnx.graph_from_place")
    @mock.patch("Geocoder.Geocoder.find_coordinates", return_value=(1, 1))
    @mock.patch("DijkstraForBike.DijkstraForBike.find_path")
    def test_give_order_to_busy_owner(self, get_graph, find_coordinates, find_path):
        system = NavigationSystem()
        system.add_owner("biker")
        owner = system.get_free_owners()[0]

        # Стал занятым
        system.give_order(owner, "address")

        self.assertRaises(OwnerStateException, system.give_order, owner, "address")


if __name__ == '__main__':
    unittest.main()
