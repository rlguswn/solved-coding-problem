tc = int(input())
for i in range(tc):
    a, b = map(int, input().split())
    result = (b-a)//2
    if b != a and b-a <= 1:
        result = -1
    print(f'#{i+1} {result}')
