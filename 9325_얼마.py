t = int(input())

for _ in range(t):
    s = int(input())
    n = int(input())
    total_money = s

    for i in range(n):
        q, p = map(int, input().split())
        total_money = total_money + (q*p)
        
    print(total_money)