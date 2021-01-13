from Geocoder import Geocoder
from GeocodingAPI import GeocodingAPI
from NavigationSystem import NavigationSystem

if __name__ == '__main__':
    test = Geocoder()
    res = test.find_address(83.673968, 53.334355)
    print()

    result = test.find_coordinates("Россия, Барнаул, ул. Балтийская 59")
    print()
