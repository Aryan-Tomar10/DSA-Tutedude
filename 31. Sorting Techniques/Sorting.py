class Sorting:
    def __init__(self):
        self.arr = []
    
    def insert(self,key):
        self.arr.append(key)

    def Bubble_sort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-i-1):
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr
    
    def insertion_sort(self):
        for i in range(1,len(self.arr)):
            j=i
            while j>0 and self.arr[j-1]>self.arr[j]:
                key = self.arr[j]
                self.arr[j] = self.arr[j-1]
                self.arr[j-1] = key
                j-=1
        return self.arr

    '''def selection_sort(self):
        def index_of_minimum(self,ind):
            smallest = self.arr[ind]
            count = ind
            for i in range(ind,len(self.arr)):
                if smallest > self.arr[i]:
                    smallest = self.arr[i]
                    count = i
            return count

        for i in range(len(self.arr)):
            ind = index_of_minimum(i)
            self.arr[i],self.arr[ind] = self.arr[ind], self.arr[i]
        return self.arr'''

    def selection_sort(self):
        for i in range(len(self.arr)):
            smallest = self.arr[i]
            count = i
            for j in range(i,len(self.arr)):
                if smallest > self.arr[j]:
                    smallest = self.arr[j]
                    count = j
            self.arr[i],self.arr[count] = self.arr[count], self.arr[i]
        return self.arr
    
    def quick_sort(self):
        def partition(low, high):
            pivot = self.arr[high]
            i = low - 1
            for j in range(low,high):
                if self.arr[j]<=pivot:
                    i+=1
                    self.arr[i],self.arr[j] = self.arr[j], self.arr[i]
            self.arr[i+1], self.arr[high] = self.arr[high],self.arr[i+1]
            return i+1
        
        def _quick_sort(low,high):
            if low<high:
                pi = partition(low,high)
                _quick_sort(low,pi-1)
                _quick_sort(pi+1,high)
        
        _quick_sort(0,len(self.arr)-1)
        return self.arr

    def merge_sort(self):
        def _merge(low,mid,high):
            left = self.arr[low:mid+1]
            right = self.arr[mid+1:high+1]

            i,j,k = 0,0,low

            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    self.arr[k] = left[i]
                    i+=1
                else:
                    self.arr[k] = right[j]
                    j+=1
                k+=1
            
            while i<len(left):
                self.arr[k] = left[i]
                i+=1
                k+=1

            while j<len(right):
                self.arr[k] = right[j]
                j+=1
                k+=1

        def _merge_sort(low,high):
            if low<high:
                mid = (low+high)//2
                _merge_sort(low,mid)
                _merge_sort(mid+1,high)
                _merge(low,mid,high)
        _merge_sort(0,len(self.arr))
        return self.arr

if __name__ == "__main__":
    s = Sorting()
    a = [4,2,6,3,9,1,0]
    for i in a:
        s.insert(i)
    print("Using Bubble Sort : ",s.Bubble_sort())
    print("Using Insertion Sort : ",s.insertion_sort())
    print("Using Selection Sort : ",s.selection_sort())
    print("Using Quick Sort : ",s.quick_sort())
    print("Using Merge Sort : ",s.merge_sort())