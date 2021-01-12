from NavigationSystem import NavigationSystem

if __name__ == '__main__':
    system = NavigationSystem()
    system.add_owner("biker")

    owners = system.get_owners()

    system.give_order(owners[0], "Россия, Барнаул, ул. Балтийская 61")
    system.perform_move()
