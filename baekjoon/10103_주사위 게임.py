r = int(input())
point = [100, 100]

for i in range(r):
    r1, r2 = map(int, input().split())

    if r1 - r2 > 0:
        point[1] -= r1
    elif r1 - r2 < 0 :
        point[0] -= r2

print(point[0])
print(point[1])