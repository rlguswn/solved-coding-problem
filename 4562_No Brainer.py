import sys

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x < y:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")