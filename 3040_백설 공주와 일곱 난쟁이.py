import sys

l = list()

for i in range(9):
    l.append(int(sys.stdin.readline()))

dif = sum(l) - 100
    
for i in range(8):
    if len(l) == 7:
        break
    for j in range(i+1, 9):
        if l[i] + l[j] == dif:
            dif -= l[i]
            l.remove(l[i])
            l.remove(dif)
            break

for i in range(7):
    print(l[i])