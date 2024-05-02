t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    result = round(sum(n) / 10)
    print(f'#{i+1} {result}')