from AStarForPedestrians import AStarForPedestrians
from Geocoder import Geocoder
from GeocodingAPI import GeocodingAPI
from NavigationSystem import NavigationSystem

if __name__ == '__main__':
    # test = Geocoder()
    # res = test.find_address(83.673968, 53.334355)
    # print()
    #
    # result = test.find_coordinates("Россия, Барнаул, ул. Балтийская 59")
    # print()

    test = AStarForPedestrians()
    # path = test.find_path(83.673968, 53.334355, 83.6829818, 53.343671)
    path = test.find_path(-84.405076, 33.787201, -84.394980, 33.764135)
    print()
