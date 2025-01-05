input_str = list(input())

result = list()

for i in input_str:
    # print(result)
    if len(result) == 0:
        result.append(i)
    elif result[-1] == i:
        result.pop()
    else:
        result.append(i)

print("".join(result))
