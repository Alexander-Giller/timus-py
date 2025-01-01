def isLucky(number: int) -> bool:
    tmp_number = number
    left_sum = 0
    right_sum = 0

    count = 0
    while tmp_number > 0:
        digit = tmp_number % 10
        if count < 3:
            right_sum += digit
        else:
            left_sum += digit

        count += 1
        tmp_number = tmp_number // 10

    return right_sum == left_sum


number = int(input())

if isLucky(number + 1) or isLucky(number - 1):
    print('Yes')
else:
    print('No')
