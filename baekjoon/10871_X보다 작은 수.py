import sys

n, X = map(int, sys.stdin.readline().split())
a = map(int, sys.stdin.readline().split())

print(' '.join(map(str, filter(lambda x:x<X, a))))