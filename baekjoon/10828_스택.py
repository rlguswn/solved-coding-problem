import sys

class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, number):
        self.stack.append(number)

    def size(self):
        return len(self.stack)
    
    def empty(self):
        if self.stack:
            return 0
        return 1
    
    def pop(self):
        if self.empty():
            return -1
        return self.stack.pop()
    
    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]

n = int(sys.stdin.readline())
s = Stack()
for i in range(n):
    command = sys.stdin.readline().strip()
    if len(command) >= 6:
        command, number = command.split()
    
    match command:
        case "push":
            s.push(number)

        case "pop":
            print(s.pop())

        case "size":
            print(s.size())

        case "empty":
            print(s.empty())
            
        case "top":
            print(s.top())