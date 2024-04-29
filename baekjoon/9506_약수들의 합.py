while(1):
    n = int(input())
    q = list()

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            q.append(i)

    if sum(q) == n:
        print(f'{n} =', end=" ")
        print(*q, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')