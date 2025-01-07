input_str = input().split(' ')

h = int(input_str[0])
w = int(input_str[1])
n = int(input_str[2])

current_position = 0
lines = 0

while n > 0:
    n -= 1
    word = input()
    word_len = len(word)
    current_position += word_len
    if current_position > w:
        current_position = word_len
        lines += 1

    current_position += 1

lines += 1

# print(lines)

if lines % h == 0:
    print(lines // h)
else:
    print(lines // h + 1)
