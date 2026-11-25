class Linear_probing:
    def __init__(self,size = 10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def _hash(self, key):
        if isinstance(key,str):
            return sum(ord(c) for c in key) % self.size
        return key % self.size
    
    def LProbing(self, key):
        idx = self._hash(key)
        i = 0
        while self.table[(idx+i)%self.size] is not None:
            i+=1
        return (idx+i)%self.size
    
    def insert(self,key):
        idx = self._hash(key)
        if self.table[idx] is not None:
            idx = self.LProbing(key)
        self.table[idx] = key
        self.count += 1
        print(f"Inserted {key} at index {idx}")
    
    def search(self, key):
        idx = self._hash(key)
        i = 0
        while self.table[(idx+i) % self.size] is not None:
            if self.table[(idx+i) % self.size] == key:
                print(f"Found {key} at index {(idx+i) % self.size}")
                return (idx+i) % self.size
            i += 1
        print(f"{key} not found")
        return -1
    
    def display(self):
        print("\nHash Table:")
        for i, val in enumerate(self.table):
            print(f"  [{i}] → {val}")




class Quadratic_probing:
    def __init__(self,size = 10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def _hash(self, key):
        if isinstance(key,str):
            return sum(ord(c) for c in key) % self.size
        return key % self.size
    
    def QProbing(self, key):
        # idx = self._hash(key)
        # i = 0
        # while self.table[(idx+i*i)%self.size] is not None:
        #     i += 1
        # return (idx+i*i)%self.size
        idx = self._hash(key)
        i = 0

        while i < self.size:
            new_idx = (idx + i*i) % self.size
            if self.table[new_idx] is None:
                return new_idx
            i += 1

        raise Exception("Hash Table Full")
    
    def insert(self,key):
        idx = self._hash(key)
        if self.table[idx] is not None:
            idx = self.QProbing(key)
        self.table[idx] = key
        self.count += 1
        print(f"Inserted {key} at index {idx}")
    
    def search(self, key):
        # idx = self._hash(key)
        # i = 0
        # while self.table[(idx+i*i) % self.size] is not None:
        #     if self.table[(idx+i*i) % self.size] == key:
        #         print(f"Found {key} at index {(idx+i*i) % self.size}")
        #         return (idx+i*i) % self.size
        #     i += 1
        # print(f"{key} not found")
        # return -1


        idx = self._hash(key)
        i = 0

        while i < self.size:
            new_idx = (idx + i*i) % self.size

            if self.table[new_idx] is None:
                break

            if self.table[new_idx] == key:
                print(f"Found {key} at index {new_idx}")
                return new_idx

            i += 1

        print(f"{key} not found")
        return -1
    
    def display(self):
        print("\nHash Table:")
        for i, val in enumerate(self.table):
            print(f"  [{i}] → {val}")




if __name__ == "__main__":
    LP = Linear_probing()
    a = [26,30,45,23,25,43,74,75,65]
    for i in a:
        LP.insert(i)
    LP.search(25)
    LP.display()