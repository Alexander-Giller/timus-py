input_args = [int(i) for i in input().split(' ')]

input_n = input_args[0]
input_k = input_args[1]


def calcProgression(n: int, k: int) -> int:
    res = 1
    hours = 0

    while k >= res and res < n:
        res = res * 2
        hours = hours + 1

    if n > res:
        remains = n - res
        hours = hours + remains // k
        if remains % k != 0:
            hours = hours + 1

    return hours


print(calcProgression(input_n, input_k))
