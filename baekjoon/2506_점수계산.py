import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
point = 0
result = 0

for i in range(n):
    if l[i]:
        point += 1
        result += point
    else:
        point = 0

print(result)