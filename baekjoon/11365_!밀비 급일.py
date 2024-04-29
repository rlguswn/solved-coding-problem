import sys

while(1):
    enc = sys.stdin.readline().split()
    dec = list()
    if enc[0] == 'END':
        break

    for i in range(len(enc)):
        dec.insert(0, ''.join(reversed(enc[i])))

    print(' '.join(dec))