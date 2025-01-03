input_str = input().split(' ')

n = int(input_str[0])
m = int(input_str[1])
y = int(input_str[2])

result = []

for i in range(m):
    if pow(i, n, m) == y:
        result.append(i)

if len(result) == 0:
    print('-1')
else:
    for res in result:
        print(res, end=' ')
