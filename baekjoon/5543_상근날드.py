import sys

h_min = float('inf')
d_min = float('inf')

for i in range(3):
    h = int(sys.stdin.readline())
    if h_min > h:
        h_min = h

for j in range(2):
    d = int(sys.stdin.readline())
    if d_min > d:
        d_min = d

result = h_min + d_min - 50

print(result)
