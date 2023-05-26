import sys

result = 0
m = -1

for i in range(10):
    x, y = map(int, sys.stdin.readline().split())
    result = result - x + y
    if result > 10000:
        result = 10000
    m = result if m < result else m
    
print(m)