from abc import ABC, abstractmethod


class PathFinder(ABC):
    def __init__(self):
        self._road_graph = None

    def _path_id_to_path_coordinates(self, path):
        """
        Добавляет к списку osm id их координаты

        :param path: list of osm id's
        :return: [{"id": int, "longitude": float, "latitude": float}, ...]
        """
        res = []

        for node in path:
            point = {
                "id": node,
                "longitude": self._road_graph.nodes._nodes[node]["x"],
                "latitude": self._road_graph.nodes._nodes[node]["y"],
            }

            res.append(point)

        return res

    def get_graph(self):
        return self._road_graph

    @abstractmethod
    def find_path(self, start_longitude: float, start_latitude: float,
                  destination_longitude: float, destination_latitude: float):
        """Построение маршрута"""
        pass
