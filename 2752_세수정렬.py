import sys

l = list(map(int, sys.stdin.readline().split()))
l.sort()

print(' '.join(map(str, l)))