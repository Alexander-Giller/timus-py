
n: int = int(input())

result = {}
for i in range(0, 101):
    result[i] = list()

for i in range(n):
    input_line = input().split(' ')
    team_id: int = int(input_line[0])
    count: int = int(input_line[1])
    result[count].append(team_id)

for task_number, teams_ids in reversed(result.items()):
    for i in teams_ids:
        print(str(i) + ' ' + str(task_number) + ' ')
