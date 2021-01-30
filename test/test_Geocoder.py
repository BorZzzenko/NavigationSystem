import unittest
from unittest import mock

from Geocoder import Geocoder, GeocodingException


class GeocoderTest(unittest.TestCase):
    def test_incorrect_coordinates_raise_geocoding_exception(self):
        geocoder = Geocoder()

        # Координаты за пределами города
        longitude = 53.3482874
        latitude = 83.7886610

        self.assertRaises(GeocodingException, geocoder.find_address, longitude, latitude)

    @mock.patch("GeocodingAPI.GeocodingAPI.find_address", return_value="address")
    def test_correct_coordinates_returns_address(self, mock):
        geocoder = Geocoder()

        # Координаты внутри города
        longitude = 83.7886610
        latitude = 53.3482874

        address = geocoder.find_address(longitude, latitude)

        self.assertIsNotNone(address)
        self.assertEqual(address, "address")

    def test_incorrect_address_raises_geocoding_exception(self):
        geocoder = Geocoder()

        # Адресс не из России
        address = "Barnaul, USA"

        self.assertRaises(GeocodingException, geocoder.find_coordinates, address)

    @mock.patch("GeocodingAPI.GeocodingAPI.find_coordinates", return_value=(2, 1))
    def test_correct_address_returns_coordinates(self, mock):
        geocoder = Geocoder()

        # Адресс содержит "Барнаул Россия"
        address = "Barnaul, Россия"

        longitude, latitude = geocoder.find_coordinates(address)

        self.assertIsNotNone(address)
        self.assertEqual(longitude, 2)
        self.assertEqual(latitude, 1)


if __name__ == '__main__':
    unittest.main()
