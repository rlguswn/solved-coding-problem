import sys

name = sys.stdin.readline().split('-')
result = ''

for i in range(len(name)):
    result += name[i][:1]

print(result)