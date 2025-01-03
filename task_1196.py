n = int(input())


teacher = set()
for i in range(n):
    teacher.add(int(input()))

k = int(input())
count = 0
for i in range(k):
    student_date = int(input())
    if student_date in teacher:
        count += 1

print(count)
