import math
import unittest
from unittest import mock

from Navigator import Navigator


class NavigatorTest(unittest.TestCase):
    def test_current_target_with_empty_path_returns_none(self):
        navigator = Navigator(1, 1)
        target = navigator.get_current_target_coordinates()

        self.assertIsNone(target)

    def test_current_target_with_correct_path_returns_coordinates(self):
        navigator = Navigator(1, 1)
        navigator.set_path([{
            "longitude": 2,
            "latitude": 1
        }])
        longitude, latitude = navigator.get_current_target_coordinates()

        self.assertEqual(longitude, 2)
        self.assertEqual(latitude, 1)

    def test_next_target_with_one_elem_in_path_returns_none(self):
        navigator = Navigator(1, 1)
        navigator.set_path(["elem"])
        target = navigator.get_next_target_coordinates()

        self.assertIsNone(target)

    def test_next_target_with_correct_path_returns_coordinates(self):
        navigator = Navigator(1, 1)
        navigator.set_path([
            {"longitude": 2, "latitude": 1},
            {"longitude": 0, "latitude": 10},
        ])
        longitude, latitude = navigator.get_next_target_coordinates()

        self.assertEqual(longitude, 0)
        self.assertEqual(latitude, 10)

    def test_compute_direction_radians(self):
        angle = Navigator.compute_direction_radians(0, 0, 1, 1)
        # Перевод из радианов в градусы
        angle = math.degrees(angle)

        self.assertEqual(angle, 45)

    def test_compute_direction_clockwise(self):
        direction = Navigator.compute_direction_clockwise(0, 0, 3, 0)
        self.assertEqual(direction, 90)

        direction = Navigator.compute_direction_clockwise(0, 0, -1, 0)
        self.assertEqual(direction, 270)

    @mock.patch("Navigator.Navigator.compute_distance", return_value=5)
    def test_navigation_tip_must_return_turn_left(self, mock):
        navigator = Navigator(1, 1)
        navigator.set_path([
            {"longitude": 1, "latitude": 2},
            {"longitude": -1, "latitude": 2},
        ])

        tip = navigator.get_navigation_tip()

        self.assertEqual(tip, "Поверните налево через 5м")

    @mock.patch("Navigator.Navigator.compute_distance", return_value=5)
    def test_navigation_tip_must_return_turn_right(self, mock):
        navigator = Navigator(1, 1)
        navigator.set_path([
            {"longitude": 3, "latitude": 2},
            {"longitude": 5, "latitude": 2},
        ])

        tip = navigator.get_navigation_tip()

        self.assertEqual(tip, "Поверните направо через 5м")

    def test_navigation_tip_without_destination_point(self):
        navigator = Navigator(1, 1)
        tip = navigator.get_navigation_tip()

        self.assertEqual(tip, "Точка назначения не задана")


if __name__ == '__main__':
    unittest.main()
