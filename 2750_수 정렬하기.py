import sys

n = int(sys.stdin.readline())
l = list()

for i in range(n):
    l.append(int(sys.stdin.readline()))

for j in range(n):
    l.sort()
    print(l.pop(0))