n = int(input())

inputValues = input().split(' ')

a = int(inputValues[0])
b = int(inputValues[1])
c = int(inputValues[2])

resSum = a + b + c
resPosition = 2
currentPosition = 2

for i in range(3, n):
    currentPosition += 1
    next = int(inputValues[currentPosition])
    a = b
    b = c
    c = next
    currentSum = a + b + c
    if currentSum > resSum:
        resPosition = currentPosition
        resSum = currentSum

print(str(resSum) + ' ' + str(resPosition))
