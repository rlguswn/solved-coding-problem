t = int(input())

for i in range(t):
    n = int(input())
    d = dict()
    
    for j in range(n):
        name, point = input().split()
        d[name] = int(point)

    print(max(d, key=d.get))
