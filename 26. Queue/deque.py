'''from collections import deque

dq = deque()

dq.append(10)
dq.appendleft(20)
dq.appendleft(30)
dq.append(40)

print(list(dq))

dq.pop()
dq.popleft()

print(list(dq))'''




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LLQ:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    def insert_front(self, data):
        new_node = Node(data)
        if self.isempty():
            self.front = self.rear = new_node
            return f"{data} inserted at front"
        new_node.next = self.front   # new → old front
        self.front.prev = new_node   # old front ← new
        self.front = new_node        # update front
        return f"{data} inserted at front"

    def insert_rear(self, data):
        new_node = Node(data)
        if self.isempty():
            self.front = self.rear = new_node
            return f"{data} inserted at rear"
        self.rear.next = new_node    # old rear → new
        new_node.prev = self.rear    # new ← old rear
        self.rear = new_node         # update rear
        new_node.next = None         # ← fix: ensure next is None
        return f"{data} inserted at rear"

    def delete_front(self):
        if self.isempty():
            return "Deque is Empty"
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None   # ← fix: clean prev pointer
        return f"{data} deleted from front"

    def delete_rear(self):
        if self.isempty():
            return "Deque is Empty"
        data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None    # ← fix: clean next pointer
        return f"{data} deleted from rear"

    def peek_front(self):
        if self.isempty():
            return "Deque is Empty"
        return f"Front: {self.front.data}"

    def peek_rear(self):
        if self.isempty():
            return "Deque is Empty"
        return f"Rear: {self.rear.data}"

    def display(self):
        if self.isempty():
            print("Deque is Empty")
            return
        temp = self.front
        print("None <->", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Driver code
dq = LLQ()
print(dq.insert_rear(10))
print(dq.insert_rear(20))
print(dq.insert_rear(30))
print(dq.insert_front(5))
print(dq.insert_front(1))

dq.display()

print(dq.peek_front())
print(dq.peek_rear())

print(dq.delete_front())
dq.display()

print(dq.delete_rear())
dq.display()