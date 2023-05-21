import sys

n = int(sys.stdin.readline())

for i in range(n):
    c, p = map(int, sys.stdin.readline().split())

    print(f'You get {c//p} piece(s) and your dad gets {c%p} piece(s).')