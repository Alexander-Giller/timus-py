input_args = input().split(' ')

t1 = int(input_args[0])
t2 = int(input_args[1])

penalty = 0
PENALTY_VALUE_MIN = 20
input_tries = input().split(' ')

for i in input_tries:
    tries = int(i)
    if tries > 0:
        penalty += PENALTY_VALUE_MIN * tries

if t1 + penalty > t2:
    print('Dirty debug :(')
else:
    print('No chance.')
