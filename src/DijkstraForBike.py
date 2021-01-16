import osmnx as ox
import networkx as nx

from PathFinder import PathFinder


class DijkstraForBike(PathFinder):
    """Поиск пути для велосипедиста алгоритмом Дейкстры"""

    def __init__(self):
        super().__init__()
        # Граф дорог для велосипедиста
        self._road_graph = ox.graph_from_place("Barnaul, Russia", network_type="bike")

    def find_path(self, start_longitude: float, start_latitude: float,
                  destination_longitude: float, destination_latitude: float):
        # Находим ближайщие вершины в графе дорог
        start_node = ox.get_nearest_node(self._road_graph, (start_latitude, start_longitude))
        end_node = ox.get_nearest_node(self._road_graph, (destination_latitude, destination_longitude))

        # Вычисялем путь алгоритмом Дейкстры
        path = nx.dijkstra_path(self._road_graph, start_node, end_node)

        # Добавляем в список координаты вершин
        path = self._path_id_to_path_coordinates(path)

        # Добавляем в список точку назначения
        path.append({
            "id": "",
            "longitude": destination_longitude,
            "latitude": destination_latitude
        })

        return path
