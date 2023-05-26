import sys

result = 0
m = -float('inf')

for i in range(4):
    x, y = map(int, sys.stdin.readline().split())
    result = result + y - x
    if m < result:
        m = result

print(m)