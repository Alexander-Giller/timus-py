n = input()

price = {
    'a': 1,
    'd': 1,
    'g': 1,
    'j': 1,
    'm': 1,
    'p': 1,
    's': 1,
    'v': 1,
    'y': 1,
    '.': 1,
    ' ': 1,

    'b': 2,
    'e': 2,
    'h': 2,
    'k': 2,
    'n': 2,
    'q': 2,
    't': 2,
    'w': 2,
    'z': 2,
    ',': 2,

    'c': 3,
    'f': 3,
    'i': 3,
    'l': 3,
    'o': 3,
    'r': 3,
    'u': 3,
    'x': 3,
    '!': 3
}

result = 0
for i in n:
    result += price[i]

print(result)
