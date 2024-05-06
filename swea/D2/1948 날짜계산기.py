t = int(input())

def func(month, day):
    d_table = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0
    for i in range(month):
        sum += d_table[i]
    return sum + day

for i in range(t):
    m1, d1, m2, d2 = map(int, input().split())
    result = func(m2, d2) - func(m1, d1) + 1
    print(f'#{i+1} {result}')