import sys

for i in range(3):
    l = list(map(int, sys.stdin.readline().split()))
    s = l[0] + l[1] + l[2] + l[3]
    if s == 0:
        print('D')
    elif s == 1:
        print('C')
    elif s == 2:
        print('B')
    elif s == 3:
        print('A')
    elif s == 4:
        print('E')