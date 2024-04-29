import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    n.sort()
    n.pop()
    n.pop(0)

    if n[2] - n[0] >= 4:
        print("KIN")
    else:
        print(sum(n))
