n = int(input())

for i in range(n):
    p = int(input())
    m, s = 0, ''

    for j in range(p):
        x, y = input().split()
        if int(x) > m:
            m = int(x)
            s = y

    print(s)