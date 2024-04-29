import sys

t = int(sys.stdin.readline())
n = 3

for i in range(t):
    l = list(map(int, sys.stdin.readline().split()))
    l.sort(reverse=True)
    print(l[n-1])
