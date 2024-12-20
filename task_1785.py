
def number_to_str(number):
    if 1 <= number <= 4:
        return "few"
    elif 5 <= number <= 9:
        return "several"
    elif 10 <= number <= 19:
        return "pack"
    elif 20 <= number <= 49:
        return "lots"
    elif 50 <= number <= 99:
        return "horde"
    elif 100 <= number <= 249:
        return "throng"
    elif 250 <= number <= 499:
        return "swarm"
    elif 500 <= number <= 999:
        return "zounds"
    else:
        return "legion"


inputNumber = int(input())
print(number_to_str(inputNumber))

