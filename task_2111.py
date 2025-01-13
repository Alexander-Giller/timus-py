n = int(input())

input_args = input().split(' ')
sorted_int_args = sorted([int(i) for i in input_args])

weight = sum(sorted_int_args)
res = 0

for i in range(n):
    road_len = sorted_int_args[i]

    res = res + weight * road_len
    weight = weight - road_len
    res = res + weight * road_len
    # print(res)

print(res)
