n = int(input())

right = abs(n)
left = 1

count = 1
result = 1

if left != right:
    if right > 1:
        count = right // 2
    result = (right + left) * count

    if right % 2 == 1:
        result += (right + 1) // 2

if n < 0:
    result = -result + 1

print(result)

