import sys

l = list()

for i in range(10):
    n = int(sys.stdin.readline()) % 42

    if l.count(n)==0:
        l.append(n)
    
print(len(l))
