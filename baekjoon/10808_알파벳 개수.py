import sys

s = sys.stdin.readline()
c = 'abcdefghijklmnopqrstuvwxyz'
l = list()

for i in c:
    l.append(str(s.count(i)))

print(' '.join(l))
