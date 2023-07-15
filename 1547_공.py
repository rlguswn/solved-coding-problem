import sys

def switching(number1, number2):
    number = cup[number1 - 1]
    cup[number1 - 1] = cup[number2 - 1]
    cup[number2 - 1] = number

n = int(sys.stdin.readline())
cup = [1, 0, 0]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    switching(x, y)

print(cup.index(1) + 1)