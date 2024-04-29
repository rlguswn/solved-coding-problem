import sys

k = int(sys.stdin.readline())

for i in range(k):
    l = list()
    count = 0
    p, m = map(int, sys.stdin.readline().split())
    for j in range(p):
        n = int(sys.stdin.readline())
        if n <= m and l.count(n) == 0:
            l.append(n)
        else:
            count += 1
    print(count)