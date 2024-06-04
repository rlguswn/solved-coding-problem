tc = int(input())
for i in range(tc):
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    q = int(input())
    print(f'#{i+1} ', end='')
    for j in range(q):
        _q = int(input()) - 1
        print(f'{s[_q%n]}{t[_q%m]} ', end='')
    print('')
        