import sys

l = [0] * (100 + 1)
total = 0

for i in range(10):
    n = int(sys.stdin.readline())
    total += n
    l[int(n/10)] += 1

print(total//10)
print(l.index(max(l))*10)
