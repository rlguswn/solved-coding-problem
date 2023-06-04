import sys

x, y = sys.stdin.readline().split()
r_x = int(''.join(reversed(x)))
r_y = int(''.join(reversed(y)))

r_sum = str(r_x + r_y)


print(int(''.join(reversed(r_sum))))