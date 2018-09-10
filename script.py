destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil","Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    for index in range(len(destinations)):
        if destination == destinations[index]:
            destination_index = index
            return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

print(get_traveler_location(test_traveler))
