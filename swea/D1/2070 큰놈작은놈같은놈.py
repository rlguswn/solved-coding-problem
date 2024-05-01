t = int(input())
for i in range(t):
    n1, n2 = map(int, input().split())
    if n1 > n2:
        r = ">"
    elif n1 < n2:
        r = "<"
    elif n1 == n2:
        r = "="
    else:
        print('error')
        continue
    print(f'#{i+1} {r}')