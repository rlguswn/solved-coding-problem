import sys

n = int(sys.stdin.readline())
ch = [sys.stdin.readline().strip() for i in range(n)]
result = list()

def move(target, index):
    for i in range(ch.index(target)):
        result.append("1")
    for j in range(ch.index(target)-index):
        result.append("4")
    ch.remove(target)
    ch.insert(index, target)

move("KBS1", 0)
move("KBS2", 1)
print(''.join(result))