import sys

student = list(range(1, 31))
for i in range(28):
    n = int(sys.stdin.readline())
    student.remove(n)

student.sort()
print(student[0])
print(student[1])
