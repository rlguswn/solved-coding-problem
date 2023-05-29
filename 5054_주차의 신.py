import sys

l = list()
my_string = ''

for i in range(8):
    l.append(int(sys.stdin.readline()))

print(sum(sorted(l, reverse=True)[0:5]))

for j in range(5):
    my_string += str(l.index(sorted(l, reverse=True)[j]) + 1)

print(' '.join(sorted(my_string)))