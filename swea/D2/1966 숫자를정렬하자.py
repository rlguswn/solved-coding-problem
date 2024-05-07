t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f'#{i+1}', end=' ')
    for j in range(n):
        print(arr[j], end=' ')
    print('')