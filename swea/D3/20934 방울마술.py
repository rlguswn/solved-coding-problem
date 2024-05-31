t = int(input())
for i in range(t):
    s, k = input().split()
    k = int(k)
    if k == 0:
        result = s.index('o')
    elif k % 2 == 1:
        result = abs(s.index('o')-1)
    elif k % 2 == 0:
        result = abs(abs(s.index('o')-1)-1)
    print(f'#{i+1} {result}')