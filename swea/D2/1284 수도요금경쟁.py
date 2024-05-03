t = int(input())
for i in range(t):
    p, q, r, s, w = map(int, input().split())
    n1 = p * w
    n2 = q if w <= r else (w-r) * s + q
    if n1 <= n2:
        print(f'#{i+1} {n1}')
    elif n1 > n2:
        print(f'#{i+1} {n2}')