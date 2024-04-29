import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
z = int(sys.stdin.readline())
n = str(x*y*z)

for i in range(10):
    print(n.count(f'{i}'))