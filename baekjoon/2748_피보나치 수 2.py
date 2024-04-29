n = int(input())
b, number, f = 0, 0, 1

for i in range(n):
    b = number
    number = f
    f = b + number

print(number)

# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     return f(n-1) + f(n-2)

