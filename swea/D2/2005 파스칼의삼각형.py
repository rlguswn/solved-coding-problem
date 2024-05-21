t = int(input())

for i in range(t):
    n = int(input())
    print(f'#{i+1}')
    for j in range(n):
        if j != 0:
            print('1 ', end='')
            print(f'{j} '*(j-1), end='')
        print('1')