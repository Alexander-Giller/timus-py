n = int(input())

inputLine = input().split(' ')

currentNumber = inputLine[0]
currentSum = 1

for i in range(1, n):
    inputNumber = inputLine[i]
    if currentNumber == inputNumber:
        currentSum += 1
    else:
        print(currentSum, currentNumber, sep = " ", end = " ")
        currentSum = 1
        currentNumber = inputNumber

print(currentSum, currentNumber, sep = " ", end = " ")
