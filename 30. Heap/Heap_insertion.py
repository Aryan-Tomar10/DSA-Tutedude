class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self,i):
        return (i-1)//2

    def _left(self,i):
        return 2*i+1

    def _right(self,i):
        return 2*i+2
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap)==0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def insert(self,key):
        self.heap.append(key)
        self._heapify_up(len(self.heap)-1)
    
    def _heapify_up(self,i):
        parent = self._parent(i)
        if i>0 and self.heap[i]>self.heap[parent]:
            self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
            self._heapify_up(parent)
    
    def delete_max(self):
        if self.is_empty():
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val
    
    def _heapify_down(self,i):
        largest = i
        left = self._left(i)
        right = self._right(i)
        n = len(self.heap)

        if left<n and self.heap[left]>self.heap[largest]:
            largest = left
        if right<n and self.heap[right]>self.heap[largest]:
            largest = right
        if largest!=i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self._heapify_down(largest)

    def build_heap(self,arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n//2-1,-1,-1):
            self._heapify_down(i)
    
    def heap_sort(self):
        backup = self.heap
        self.build_heap(self.heap)
        sorted_arr = []
        while not self.is_empty():
            sorted_arr.append(self.delete_max())
        self.heap = backup
        return sorted_arr[::-1]

    def display(self):
        if self.is_empty():
            print("Heap is empty")
            return
        print(f"Heap : {self.heap}")
        print(f"Max (root) : {self.heap[0]}")


class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self,i):
        return (i-1)//2
    
    def _left(self,i):
        return 2*i+1

    def _right(self,i):
        return 2*i+2
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap)==0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def heapify_up(self,i):
        parent = self._parent(i)
        if i>0 and self.heap[i]<self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.heapify_up(parent)
    
    def insert(self,key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    def heapify_down(self,i):
        smallest = i
        left = self._left(i)
        right = self._right(i)
        n = len(self.heap)

        if left<n and self.heap[left]<self.heap[smallest]:
            smallest = left
        if right<n and self.heap[right]<self.heap[smallest]:
            smallest = right
        if smallest!=i:
            self.heap[i],self.heap[smallest] = self.heap[smallest], self.heap[i]
            return self.heap[smallest]

    def delete_max(self):
        if self.is_empty():
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val
    
    def display(self):
        if self.is_empty():
            print("Heap is empty")
            return
        print(f"Heap : {self.heap}")
        print(f"Min (root) : {self.heap[0]}")

if __name__ == "__main__":
    MaxH = MaxHeap()
    for x in [10, 20, 30, 40, 50, 25]:
        MaxH.insert(x)
        print(f"Insert {x:2d} → {MaxH.heap}")
    print("Sorted Heap : ",MaxH.heap_sort())
    MaxH.display()

    MinH = MinHeap()
    for x in [10, 20, 30, 40, 50, 25]:
        MinH.insert(x)
        print(f"Insert {x:2d} → {MinH.heap}")
    print("Sorted Heap : ",MaxH.heap_sort())
    MinH.display()