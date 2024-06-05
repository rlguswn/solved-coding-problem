tc = int(input())

for i in range(tc):
    n = int(input())
    pi = list(map(int, input().split()))
    for j in range(n):
        pi.remove(int(pi[j] / 3 * 4))
    result = ' '.join(list(map(str, pi)))
    print(f'#{i+1} {result}')