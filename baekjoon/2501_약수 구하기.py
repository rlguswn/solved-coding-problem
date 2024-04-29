import sys

n, k = map(int, sys.stdin.readline().split())
l = list()

for i in range(1, n+1):
    if n % i == 0:
        l.append(i)

try:
    print(l[k-1])
except:
    print(0)