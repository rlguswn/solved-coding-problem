import sys

class Queue():
    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def enqueue(self, value):
        self.in_queue.append(value)

    def dequeue(self):
        if not self.out_queue:
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())
        if self.out_queue:
            return self.out_queue.pop()
        
    def size(self):
        return len(self.in_queue) + len(self.out_queue)
    
    def top(self):
        if not self.out_queue:
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())
        if self.out_queue:
            return self.out_queue[-1]

n = int(sys.stdin.readline())
card = Queue()
for i in range(1, n+1):
    card.enqueue(i)

while(card.size() > 1):
    card.dequeue()
    card.enqueue(card.dequeue())

print(card.top())