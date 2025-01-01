droids_input = input().split(' ')

n = int(droids_input[0])
k = int(droids_input[1])

balls_input = input().split(' ')

balls_remains = 0
droid_remains = 0

for balls_str in balls_input:
    balls = int(balls_str)
    if balls > k:
        balls_remains += balls - k
    else:
        droid_remains += k - balls

print(str(balls_remains) + ' ' + str(droid_remains))
