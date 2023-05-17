t = int(input())

for j in range(t):
    n = int(input())

    total_c, total_g = 0, 0

    for i in range(n):
        c, g = input().split()
        total_c += int(c)
        g = float(c) * float(g)
        total_g += g

    ave_g = total_g / total_c

    print(f'{total_c} {ave_g:.1f}')