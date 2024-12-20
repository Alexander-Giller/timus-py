n = int(input())

minutesLeft = 4 * 60
tasksLeft = 12 - n

if minutesLeft >= tasksLeft * 45:
    print("YES")
else:
    print("NO")

