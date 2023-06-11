import sys

n = int(sys.stdin.readline())
n2 = n
count = 0

while(1):
    a = n2//10
    b = n2%10

    n2 = a + b

    n2 = (b*10) + (n2%10)
    count += 1

    if n == n2:
        break

print(count)