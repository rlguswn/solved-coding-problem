t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    candy = sorted(list(map(int, input().split())))
    result = 1000000000
    for j in range(n-k+1):
        d = candy[j+k-1] - candy[j]
        if result > d:
            result = d
    print(f'#{i+1} {result}')