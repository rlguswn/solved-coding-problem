import sys

s = sys.stdin.readline()

for i in ['a', 'e', 'i', 'o', 'u']:
    s = s.replace(i, '1')

print(s.count('1'))