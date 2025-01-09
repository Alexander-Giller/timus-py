n = int(input())

res = 0
current_sum = 0

for i in range(n):
    value = int(input())
    current_sum += value
    if current_sum > res:
        res = current_sum
    if current_sum < 0:
        current_sum = 0

print(res)
