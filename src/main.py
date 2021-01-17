from NavigationSystem import NavigationSystem
import osmnx as ox

if __name__ == '__main__':
    system = NavigationSystem()
    system.add_owner("driver")
    owner = system.get_owners()[0]

    system.give_order(owner, "59, Балтийская улица, Барнаул, Россия")

    navigator = owner.get_navigator()
    path = navigator.get_path()
    path.pop()
    path = [x['id'] for x in path]

    while navigator.get_location() != navigator.get_destination():
        print("Location: ", *system.get_location(owner))
        print("next target: ", owner.get_navigator().get_current_target_coordinates())
        print("Nav tip:", system.get_current_tip(owner))

        system.perform_move()

    graph = ox.graph_from_place("Barnaul, Russia", network_type="drive")
    fig, ax = ox.plot_graph_route(graph, path, node_size=1)
