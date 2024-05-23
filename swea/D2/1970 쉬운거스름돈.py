t = int(input())
money_table = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(t):
    money = int(input())
    cnt = [0 for _ in range(8)]
    for j in range(8):
        cnt[j] = money // money_table[j]
        money %= money_table[j]
    print(f'#{i+1}')
    print(' '.join(map(str, cnt)))