input_str = list(input())

symbols = {}

for i in input_str:
    if symbols.get(i) is None:
        symbols[i] = 1
    else:
        symbols[i] += 1

max_symbol = None
max_power = 0

for key, value in symbols.items():
    if value > max_power:
        max_symbol = key
        max_power = value

print(max_symbol)
