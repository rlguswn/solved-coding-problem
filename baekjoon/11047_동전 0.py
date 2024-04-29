import sys

n, k = map(int, sys.stdin.readline().split())
l = list()
result = 0

for i in range(n):
    l.append(int(sys.stdin.readline()))

l.sort(reverse=True)

for i in range(n):
    result += k // l[i]
    k %= l[i]

print(result)