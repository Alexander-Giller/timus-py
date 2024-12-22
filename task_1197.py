from collections import namedtuple

Pair = namedtuple("Pair", ["x", "y"])

def getCoordinate(c) -> int:
    # convert character to acii code - ('a' - 1) code.
    return ord(c) - 96


n = int(input())

horseMoves = {
    Pair(1, 2),
    Pair(-1, 2),
    Pair(1, -2),
    Pair(-1, -2),
    Pair(2, 1),
    Pair(-2, 1),
    Pair(2, -1),
    Pair(-2, -1)
}

for i in range(n):
    position = input()
    x = getCoordinate(position[0])
    y = int(position[1])
    coordinate = Pair(x, y)
    result = 8
    for move in horseMoves:
        potentialPosition = Pair(coordinate.x + move.x, coordinate.y + move.y)
        #print(potentialPosition)
        if (potentialPosition.x < 1 or potentialPosition.y < 1 or
                potentialPosition.x > 8 or potentialPosition.y > 8):
            result -= 1
    print(result)
