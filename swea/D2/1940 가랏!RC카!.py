t = int(input())
for i in range(t):
    n = int(input())
    s = 0
    d = 0
    for j in range(n):
        c = input()
        if c != '0':
            c1, c2 = map(int, c.split())
            if c1 == 1:
                s += c2
            elif c1 == 2:
                s -= c2
                if s < 0:
                    s = 0
        d += s
    print(f'#{i+1} {d}')