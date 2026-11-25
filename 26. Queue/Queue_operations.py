size = int(input("Enter the size of Queue: "))
queue = []

def enqueue(x):
    if len(queue) == size:
        return "Queue is Full"
    queue.append(x)
    return f"{x} enqueued successfully"

def dequeue():
    if len(queue) == 0:
        return "Queue Underflow, can't dequeue"
    return queue.pop(0)

def isfull():
    return len(queue) == size

def isempty():
    return len(queue) == 0

def display():
    if isempty():
        return "Queue is empty"
    return queue

# Driver code
print(enqueue(1))   # 1 enqueued successfully
print(enqueue(2))   # 2 enqueued successfully
print(enqueue(3))   # 3 enqueued successfully
print(enqueue(4))   # Queue is Full (if size=3)
print(display())    # [1, 2, 3]
print(dequeue())    # 1
print(display())    # [2, 3]
print(enqueue(1))   # 1 enqueued successfully
print(display())    # [2, 3]
print(isfull())     # False
print(isempty())    # False