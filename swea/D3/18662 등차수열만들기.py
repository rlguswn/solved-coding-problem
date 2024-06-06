tc = int(input())
for i in range(tc):
    x, y, z = map(int, input().split())
    result = abs(2*y - x - z)/2
    print(f'#{i+1} {result}')