import math
import sys
from abc import ABC, abstractmethod


class PathFinder(ABC):
    def __init__(self):
        self._road_graph = None

    def _path_id_to_path_coordinates(self, path):
        res = []

        for node in path:
            point = {
                "id": node,
                "longitude": self._road_graph.nodes._nodes[node]["x"],
                "latitude": self._road_graph.nodes._nodes[node]["y"],
            }

            res.append(point)

        return res

    def _find_nearest_node(self, longitude, latitude):
        nodes = self._road_graph.nodes._nodes

        min_id = 0
        min_distance = sys.maxsize
        min_x = 0
        min_y = 0

        for node in nodes.keys():
            lat = nodes[node]["y"]
            lon = nodes[node]["x"]

            # distance = ((longitude - lon) ** 2) + ((latitude - lat) ** 2) ** 0.5

            dlat = latitude - lat
            dlon = longitude - lon
            dist2 = dlat * dlat + dlon * dlon
            distance = math.sqrt(dist2)

            if distance < min_distance:
                min_id = node
                min_distance = distance
                min_x = lon
                min_y = lat

        return min_id


    @abstractmethod
    def find_path(self, start_longitude: float, start_latitude: float,
                  destination_longitude: float, destination_latitude: float):
        pass
