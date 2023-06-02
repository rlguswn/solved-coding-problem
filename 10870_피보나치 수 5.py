import sys

n = int(sys.stdin.readline())
l = [0, 1]

for i in range(n-1):
    l.append(l[i] + l[i+1])

print(l[n])