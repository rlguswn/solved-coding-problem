import sys

i = 0
n = [''] * 5
while(1):
    i+=1
    n[0] = int(sys.stdin.readline())
    if n[0] == 0:
        break
    n[1] = n[0] * 3
    n[2] = n[1] // 2 + n[1] % 2
    n[3] = n[2] * 3
    n[4] = n[3] // 9
    if n[0] % 2 == 0:
        number_type = 'even'
    else:
        number_type = 'odd'
    print(f'{i}. {number_type} {n[4]}')