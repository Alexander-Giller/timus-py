n = int(input())

penguinsCollection = {}

for i in range(n):
    inputPenguin = input()
    if penguinsCollection.get(inputPenguin) is None:
        penguinsCollection[inputPenguin] = 1
    else:
        penguinsCollection[inputPenguin] = penguinsCollection[inputPenguin] + 1

resultPenguin = None
resultCount = 0
for penguin, number in penguinsCollection.items():
    if resultCount < number:
        resultPenguin = penguin
        resultCount = number

print(resultPenguin)


