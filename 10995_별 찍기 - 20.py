import sys

n = int(sys.stdin.readline())

for i in range(n):
    if i % 2 == 0:
        print('* '*(n-1)+'*')
    else:
        print(' *'*(n-1)+' *')