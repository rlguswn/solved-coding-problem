import sys

t = int(sys.stdin.readline())
for i in range(t):
    count = 0
    text = "YES"
    s = sys.stdin.readline().strip()
    for j in s:
        if j == "(":
            count += 1
        elif j == ")":
            count -= 1
        if count < 0:
            text = "NO"
            break
    if count != 0:
        text = "NO"
    print(text)
