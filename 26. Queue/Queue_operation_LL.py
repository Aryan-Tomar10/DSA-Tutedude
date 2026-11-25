class Queue:
    def __init__(self, data):
        self.data = data
        self.next = None        # fix 1

class LinkedListQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, x):
        new_node = Queue(x)
        if self.head is None:
            self.head = new_node
            return f"{x} enqueued"
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"{x} enqueued"

    def dequeue(self):
        if self.head is None:
            return "Queue is Empty"
        data = self.head.data   # fix 3
        self.head = self.head.next
        return f"{data} dequeued"

    def isempty(self):
        return self.head is None

    def display(self):
        if self.isempty():
            print("Queue is Empty")
            return
        temp = self.head        # fix 2
        while temp:
            print(temp.data, '->', end=' ')
            temp = temp.next
        print("None")


# Driver code
LLQ = LinkedListQueue()
print(LLQ.enqueue(10))
print(LLQ.enqueue(20))
print(LLQ.enqueue(30))
print(LLQ.enqueue(40))
print(LLQ.enqueue(50))
LLQ.display()

print(LLQ.dequeue())
LLQ.display()

print(LLQ.isempty())

print(LLQ.dequeue())
print(LLQ.dequeue())  # Queue is Empty

print(LLQ.isempty())
LLQ.display()