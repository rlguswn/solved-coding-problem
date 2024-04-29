import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())

    print(''.join(list(map(str, range(n, m+1)))).count('0'))
