t = int(input())
for i in range(t):
    tn = int(input())
    n = list(map(int, input().split()))
    cnt = [0 for _ in range(101)]
    for j in n:
        cnt[j] += 1
    cnt.reverse()
    result = 100 - cnt.index(max(cnt))
    print(f'#{tn} {result}')