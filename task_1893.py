input_str = input()

symbol = input_str[-1]
number = int(input_str[0: -1])

CONST_WINDOW = 'window'
CONST_AISLE = 'aisle'
CONST_NEITHER = 'neither'

if (symbol == 'A' or
        (1 <= number <= 2 and symbol == 'D') or
        (3 <= number <= 20 and symbol == 'F') or
        (21 <= number <= 65 and symbol == 'K')):
    print(CONST_WINDOW)

elif (1 <= number <= 20 or
      symbol in ['C', 'D', 'G', 'H']):
    print(CONST_AISLE)

else:
    print(CONST_NEITHER)
