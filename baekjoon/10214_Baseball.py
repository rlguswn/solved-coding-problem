t = int(input())
sum_y, sum_k = 0, 0

for i in range(t):
    for j in range(9):
        y, k = map(int, input().split())
        sum_y += y
        sum_k += k

    print('Yonsei' if sum_y > sum_k else 'Draw' if sum_y == sum_k else 'Korea')
    