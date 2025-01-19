input_args = [int(i) for i in input().split(' ')]

x = input_args[0]
y = input_args[1]
c = input_args[2]

if x + y < c:
    print("Impossible")
else:
    if x >= c:
        a = c
        b = 0
    else:
        a = x
        b = c - a
    print(str(a) + " " + str(b))
