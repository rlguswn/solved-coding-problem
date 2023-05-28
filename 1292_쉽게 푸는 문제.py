import sys

l = list()
start, end = map(int, sys.stdin.readline().split())

for i in range(1, end+1):

    if len(l)<end:
        for j in range(i):
            l.append(i)
            if len(l)==end:
                break

for _ in range(start-1):
    l.pop(0)

print(sum(l))