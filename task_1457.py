n = int(input())

input_args = input().split(' ')
int_args = [int(i) for i in input_args]

res = sum(int_args) / n

print("{:.6f}".format(res))
