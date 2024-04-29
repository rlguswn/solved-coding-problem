import sys

n = int(sys.stdin.readline())
result = n * (n-1)
if result < 0:
    result = 0
print(result)