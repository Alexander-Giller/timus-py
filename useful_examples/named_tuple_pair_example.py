from collections import namedtuple

Pair = namedtuple("Pair", ["x", "y"])

available_coordinates = {
    Pair(1, 2),
    Pair(-1, 2),
    Pair(1, -2),
    Pair(-1, -2),
    Pair(2, 1),
    Pair(-2, 1),
    Pair(2, -1),
    Pair(-2, -1)
}

print(available_coordinates)
