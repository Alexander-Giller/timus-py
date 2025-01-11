n = int(input())
input_args = input().split(' ')

int_args = [int(i) for i in input_args]
int_args.sort()

res = 0

for i in range(n // 2 + 1):
    res += int_args[i] // 2 + 1

print(res)

