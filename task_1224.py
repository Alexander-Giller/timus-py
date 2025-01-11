input_params = input().split(' ')

n = int(input_params[0])
m = int(input_params[1])

res = 0

if n > m:
    res = 2 * (m - 1) + 1
else:
    res = 2 * (n - 1)

print(res)
