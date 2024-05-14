t = int(input())
for i in range(t):
    h1, m1, h2, m2 = map(int, input().split())
    total_h = h1 + h2
    total_m = m1 + m2

    if total_m > 60:
        total_h += 1
        total_m -= 60
    if total_h > 12:
        total_h -= 12

    print(f'#{i+1} {total_h} {total_m}')