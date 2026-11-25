class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # fixed size array
        self.front = -1
        self.rear = -1

    def isfull(self):
        return (self.rear + 1) % self.size == self.front
    
    def isempty(self):
        return self.front == -1
    
    def enqueue(self, x):
        if self.isfull():
            return "Queue is Full"
        elif self.isempty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size  # wrap around
        self.queue[self.rear] = x
        return f"{x} enqueued"

    def dequeue(self):
        if self.isempty():
            return "Queue is Empty"
        data = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:  # only one element was left
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size  # wrap around
        return f"{data} dequeued"



    def display(self):
        if self.isempty():
            return "Queue is Empty"
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return result


# Driver code
cq = CircularQueue(4)

print(cq.enqueue(10))   # 10 enqueued
print(cq.enqueue(20))   # 20 enqueued
print(cq.enqueue(30))   # 30 enqueued
print(cq.enqueue(40))   # 40 enqueued
print(cq.enqueue(50))   # Queue is Full

print(cq.display())     # [10, 20, 30, 40]

print(cq.dequeue())     # 10 dequeued
print(cq.dequeue())     # 20 dequeued

print(cq.display())     # [30, 40]

print(cq.enqueue(50))   # 50 enqueued  ← reuses freed space
print(cq.enqueue(60))   # 60 enqueued  ← reuses freed space

print(cq.display())     # [30, 40, 50, 60]