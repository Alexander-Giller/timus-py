left = int(input())
right = int(input())

if left > right:
    tmp = left
    left = right
    right = tmp

result = (right - left) // 2

if right % 2 == 1 or left % 2 == 1:
    result += 1

print(result)
