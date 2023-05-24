import sys

n = list(map(int, (sys.stdin.readline().split())))

print(sum(map(lambda x:x*x, n)) % 10)
