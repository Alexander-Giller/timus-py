ones = set()
ones.add(1)

maxValue = pow(2, 31)
step = 0
currentPositionWithOne = 1
currentValue = 0

while 1:
    step += 1
    currentPositionWithOne += step
    ones.add(currentPositionWithOne)
    currentValue += step
    if currentValue >= maxValue:
        break

n = int(input())

for i in range(n):
    inputPosition = int(input())
    if inputPosition in ones:
        print(1, ' ')
    else:
        print(0, ' ')
