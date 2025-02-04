import sys

n = int(sys.stdin.readline())
nlist = set(sys.stdin.readline().split())
m = int(sys.stdin.readline())
mlist = list(sys.stdin.readline().split())

for i in mlist:
    print(1 if i in nlist else 0)