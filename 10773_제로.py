import sys

k = int(sys.stdin.readline())
l = list()

for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        l.pop()
    else:
        l.append(n)

print(sum(l))
