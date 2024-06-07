tc = int(input())
for i in range(tc):
    a, b = map(int, input().split())
    if a==b:
        result = a
    else:
        result = 1
    print(f'#{i+1} {result}')
