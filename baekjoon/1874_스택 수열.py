import sys

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
    
    def empty(self):
        if self.stack:
            return 0
        return 1
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1
    
    def size(self):
        return len(self.stack)

n = int(sys.stdin.readline())
number = Stack()
for i in range(n, 0, -1):
    number.push(i)

s = Stack()
result = []
for i in range(n):
    next = int(sys.stdin.readline())
    if not number.empty():
        while number.top() != -1 and number.top() <= next:
            s.push(number.pop())
            result.append("+")
    if s.top() == next:
        s.pop()
        result.append("-")

if len(result) == n*2:
    for i, v in enumerate(result):
        print(v)
else:
    print("NO")