from NavigationSystem import NavigationSystem

if __name__ == '__main__':
    system = NavigationSystem()
    system.add_owner("driver")
    owner = system.get_owners()[0]

    system.give_order(owner, "59, Балтийская улица, Барнаул, Россия")

    navigator = owner.get_navigator()

    while navigator.get_location() != navigator.get_destination():
        print("Location: ", *system.get_location(owner))
        print("next target: ", owner.get_navigator().get_current_target_coordinates())

        system.perform_move()
