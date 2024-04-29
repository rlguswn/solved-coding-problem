import sys

n = int(sys.stdin.readline())
i = 1
sum = 0
count = 0

while(1):
    if n == sum:
        break
    if sum + i > n:
        i = 1
    sum += i
    i += 1
    count += 1

print(count)