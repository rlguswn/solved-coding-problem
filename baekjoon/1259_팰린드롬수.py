import sys

while(1):
    n = str(int(sys.stdin.readline()))
    if n=="0":
        break
    if n==n[::-1]:
        print("yes")
    else:
        print("no")