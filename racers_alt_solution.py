def non_winners(races):
    # Set to hold all drivers present in the dictionary
    all_drivers = set()
    # Set to hold drivers who won at least one race
    winners = set()
    
    for podium in races.values():
        # Add each driver to set of all drivers
        # all_drivers.add(podium[0])
        # all_drivers.add(podium[1])
        # all_drivers.add(podium[2])
        # for racer in podium:
        all_drivers.update(podium)


        # Only add the winner to the set of winners
        winners.add(podium[0])

    # print(winners)
    # print(all_drivers)

    non_winners = set()

    for driver in all_drivers:
        if driver not in winners:
            non_winners.add(driver)

    # print(non_winners)
    return non_winners

    # non_winners = set()

    # for dirver in all_drivers:
    #     if driver not in winners:

    # Set to hold drivers who never won
    # non_winners = set()

    # for driver in all_drivers:
    #     if driver not in winners:
    #         non_winners.add(driver)
            
    return all_drivers

races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
assert non_winners(races_1) == {"Latifi", "Stroll"}

races_2 = {
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
}
assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

races_3 = {
    "Monaco": ("Leclerc", "Verstappen", "Sainz"),
    "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
    "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
}
# If all drivers present in the dictionary won a race
# then the return value should be an empty set
assert non_winners(races_3) == set()
print("All tests passed! Discuss time/space complexity if time remains")
