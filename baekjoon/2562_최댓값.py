import sys

n = list()

for _ in range(9):
    n.append(int(sys.stdin.readline()))

print(max(n))
print(n.index(max(n))+1)
