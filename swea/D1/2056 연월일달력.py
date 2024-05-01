t = int(input())

for i in range(t):
    ymd = str(input())
    print(f'#{i+1}', end=' ')
    if int(ymd[4:6]) in {1, 3, 5, 7, 8, 10, 12} and int(ymd[6:8]) in range(1, 32):
        print(f'{ymd[0:4]}/{ymd[4:6]}/{ymd[6:8]}')
    elif int(ymd[4:6]) in {4, 6, 9, 11} and int(ymd[6:8]) in range(1, 31):
        print(f'{ymd[0:4]}/{ymd[4:6]}/{ymd[6:8]}')
    elif int(ymd[4:6]) == 2 and int(ymd[6:8]) in range(1, 29):
        print(f'{ymd[0:4]}/{ymd[4:6]}/{ymd[6:8]}')
    else:
        print(-1)