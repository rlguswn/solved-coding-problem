t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    n.sort()
    print(f'#{i+1}', end=' ')
    print(n[len(n)-1])