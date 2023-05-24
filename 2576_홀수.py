import sys

l = list()

for _ in range(7):
    count = 0
    n = int(sys.stdin.readline())
    if n%2!=0:
        l.append(n)

if l:
    print(sum(l))
    print(min(l))
else:
    print(-1)