import sys

s = sys.stdin.readline()
length = len(s)-1

t = length // 10

for i in range(t):
    print(s[0:10])
    s = s.replace(s[0:10], '')

if length % 10 != 0:
    print(s)