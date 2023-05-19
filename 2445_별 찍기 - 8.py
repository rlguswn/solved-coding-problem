n = int(input())

for i in range(1, n+1):
    print(('*'*i).ljust(n, ' '), end='')
    print(('*'*i).rjust(n, ' '))

for i in range(1, n):
    print(('*'*(n-i)).ljust(n, ' '), end='')
    print(('*'*(n-i)).rjust(n, ' '))