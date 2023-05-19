import sys
n = int(sys.stdin.readline())

l = list()
l.append(-n)

for i in range(n):
    l.append(int(sys.stdin.readline()))

print(sum(l)+1)