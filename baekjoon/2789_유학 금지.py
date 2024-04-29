import sys

s = list('CAMBRIDGE')

r = sys.stdin.readline()
for i in s:
    r = r.replace(i, '')

print(r)