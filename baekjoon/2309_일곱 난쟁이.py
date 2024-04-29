import sys

l = list()
for i in range(9):
    l.append(int(sys.stdin.readline()))

s = sum(l)
dif = s - 100

for i in range(9):
    for j in range(9):
        if i != j and dif == l[i]+l[j]:
            dif -= l[i]
            l.remove(l[i])
            l.remove(dif)
            break
    if len(l)==7:
        l.sort()
        break

for i in range(7):
    print(l[i])
