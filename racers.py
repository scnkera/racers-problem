def non_winners(races):

    unique_racers = set()

    for racers in races.values():
        unique_racers.update(racers)
    # for racers in races.values():
        unique_racers.discard(racers[0])

    # for racers in racers.items():

    print(unique_racers)
    return(unique_racers)








    unique_racers = set()

    #option 1

    # for racers in races.values():
    #     for racer in racers:
    #         unique_racers.add(racer)


    # option 2
    # for racers in races.values():
    #     unique_racers.update(racers)
    


    # for racers in races.values():
    #     unique_racers.discard(racers[0])

    
    # print(unique_racers)
    # return unique_racers


non_winners({
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
})
    
    # hash_table = {}
    # racers_list = []

    # for racers in races_1.values():
    #     unique_racers = set(racers)

    #     # for racer in unique_racers:
    #     #     if racer not in racers_list:
    #     #         racers_list.append(racer)

    #     print(unique_racers)

    # return unique_racers
    


# races_1 = {
#     "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
#     "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
#     "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
# }
# assert non_winners(races_1) == {"Latifi", "Stroll"}

# races_2 = {
#     "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
# }
# assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

# races_3 = {
#     "Monaco": ("Leclerc", "Verstappen", "Sainz"),
#     "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
#     "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
# }
# # If all drivers present in the dictionary won a race
# # then the return value should be an empty set
# assert non_winners(races_3) == set()

# print("All tests passed! Discuss time/space complexity if time remains")