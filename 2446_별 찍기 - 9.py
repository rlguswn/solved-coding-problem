n = int(input())

for i in range(n):
    print(('*'*(2*n-2*i-1)).rjust(2*n-1-i))

for i in range(1, n):
    print(('*'*(2*i+1)).rjust(i+n))
