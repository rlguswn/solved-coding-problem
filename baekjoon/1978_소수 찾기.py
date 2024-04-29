import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
result = n

for i in range(n):
    if l[i] == 1:
        result -= 1
    else:
        for j in range(2, l[i]):
            if l[i] % j == 0:
                result -= 1
                break

print(result)