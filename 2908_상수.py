import sys

a, b = sys.stdin.readline().split()

a2 = int(''.join(reversed(a)))
b2 = int(''.join(reversed(b)))

print(a2 if a2>b2 else b2)