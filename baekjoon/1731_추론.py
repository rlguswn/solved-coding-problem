import sys

n = int(sys.stdin.readline())
number = [int(sys.stdin.readline()) for _ in range(n)]

if number[1] - number[0] == number[2] - number[1]:
    q = number[1] - number[0]
    print(number[n-1] + q)
elif number[1] / number[0] == number[2] / number[1]:
    q = int(number[1] / number[0])
    print(number[n-1] * q)