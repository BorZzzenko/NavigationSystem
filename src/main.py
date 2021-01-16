from AStarForPedestrians import AStarForPedestrians
import osmnx as ox

from DijkstraForCar import DijkstraForCar
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

    test = DijkstraForCar()
    path = test.find_path(83.6736118, 53.3337519, 83.6850590, 53.3443563)
    graph = ox.graph_from_place("Barnaul, Russia", network_type="drive")

    path = [x['id'] for x in path]

    fig, ax = ox.plot_graph_route(graph, path, node_size=0)
