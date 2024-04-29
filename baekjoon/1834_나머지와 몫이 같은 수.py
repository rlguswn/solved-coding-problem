import sys

n = int(sys.stdin.readline())
result = 0

if n > 1:
    for i in range(1, n):
        result = result + (n*i + i)
    print(result)
else:
    print(0)