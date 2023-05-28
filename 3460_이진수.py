import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = bin(int(sys.stdin.readline()))
    l = list()
    p = 0

    for i in range(len(n)-2):
        if n[len(n)-1-i]=='1':
            l.append(p)
        p += 1

    print(' '.join(map(str, l)))