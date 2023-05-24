import sys

n = int(sys.stdin.readline())
l = list(map(float, sys.stdin.readline().split()))
l2 = list()

for i in range(n):
    l2.append((l[i] / max(l))*100)

print(sum(l2)/n)