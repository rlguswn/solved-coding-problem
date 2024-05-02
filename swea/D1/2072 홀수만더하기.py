t = int(input())
for i in range(t):
    sum = 0
    n = list(map(int, input().split()))
    for j in n:
        if j%2==1:
            sum += j
    print(f'#{i+1} {sum}')