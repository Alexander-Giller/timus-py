results = {
    1: 2,
    2: 2,
    3: 4
}

for i in range(4, 46):
    results[i] = results[i - 1] + results[i - 2]

n = int(input())
print(results[n])
