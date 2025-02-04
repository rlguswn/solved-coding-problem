import sys

class Queue():
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, value):
        self.in_stack.append(value)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack.pop()
        return -1
    
    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def empty(self):
        if self.in_stack or self.out_stack:
            return 0
        return 1

    def front(self):
        if self.out_stack:
            return self.out_stack[-1]
        elif self.in_stack:
            return self.in_stack[0]
        return -1

    def back(self):
        if self.in_stack:
            return self.in_stack[-1]
        elif self.out_stack:
            return self.out_stack[0]
        return -1

n = int(sys.stdin.readline())
q = Queue()
for i in range(n):
    command = sys.stdin.readline().strip()
    if len(command) >= 6:
        command, number = command.split()

    match command:
        case "push":
            q.push(number)

        case "pop":
            print(q.pop())

        case "size":
            print(q.size())

        case "empty":
            print(q.empty())

        case "front":
            print(q.front())

        case "back":
            print(q.back())