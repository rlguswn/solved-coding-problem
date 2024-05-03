t = int(input())
for i in range(t):
    xn = 0
    arr = list()
    n = int(input())
    while(1):
        xn += n
        cxn = xn
        for _ in range(len(str(xn))):
            arr.append(cxn % 10)
            cxn = int(cxn / 10)
        if len(list(set(arr))) == 10:
            print(f'#{i+1} {xn}')
            break
