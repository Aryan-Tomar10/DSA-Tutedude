class Node:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.next = None

class Chaining_Technique_HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [None]*size
        self.count = 0

    def _hash(self, key):
        if isinstance(key,str):
            return sum(ord(c) for c in key) % self.size
        return key % self.size

    def insert(self, key, value = None):
        idx = self._hash(key)
        node = self.table[idx]

        while node:
            if node.key == key:
                node.value = value
                print(f"Updated  : key={key}, value={value} at index {idx}")
                return
            node = node.next

        new_node = Node(key,value)
        new_node.next = self.table[idx]
        self.table[idx] = new_node
        self.count +=1
        print(f"Printed  : key={key}, value={value} at index {idx}")

    def delete(self,key):
        idx = self._hash(key)
        node = self.table[idx]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[idx] = node.next
                self.count-=1
                print(f"Deleted  : key={key}, from index {idx}")
                return True
            prev = node
            node = node.next
        
        print(f"Not Found: key={key} for deletion")
        return False
    
    def search(self,key):
        idx = self._hash(key)
        node = self.table[idx]

        while node:
            if node.key == key:
                print(f"Found  : key={key},value = {node.value} at index {idx}")
                return node.value
            node = node.next
        print(f"Deleted  : key={key}")
        return None
    
    def load_factor(self):
        return self.count/self.size
    
    def display(self):
        print("\nHash Table:")
        print("-" * 40)
        for i in range(self.size):
            print(f"  [{i:2d}]", end=" → ")
            node = self.table[i]
            if node is None:
                print("None")
            else:
                chain = []
                while node:
                    if node.value is not None:
                        chain.append(f"({node.key}:{node.value})")
                    else:
                        chain.append(f"({node.key})")
                    node = node.next
                print(" → ".join(chain))
        print(f"\nTotal Elements : {self.count}")
        print(f"Load Factor    : {self.load_factor():.2f}")
        print("-" * 40)
    

if __name__ == "__main__":
    # ── Example 1: Integer Keys ───────────────
    print("=" * 45)
    print("    Chaining with Integer Keys")
    print("    Table Size = 7")
    print("=" * 45)

    cht = Chaining_Technique_HashTable(size=7)

    # insert elements
    print("\nInserting elements:")
    print("-" * 40)
    keys = [10, 20, 30, 25, 15, 7, 14, 21]
    for k in keys:
        cht.insert(k)

    cht.display()

    # search
    print("\nSearching:")
    print("-" * 40)
    cht.search(25)
    cht.search(14)
    cht.search(99)

    # delete
    print("\nDeleting:")
    print("-" * 40)
    cht.delete(20)
    cht.delete(99)
    cht.display()

    # ── Example 2: Key-Value Pairs ────────────
    print("\n" + "=" * 45)
    print("    Chaining with Key-Value Pairs")
    print("    Table Size = 5")
    print("=" * 45)

    cht2 = Chaining_Technique_HashTable(size=5)

    print("\nInserting key-value pairs:")
    print("-" * 40)
    cht2.insert("name",  "Aryan")
    cht2.insert("age",   21)
    cht2.insert("city",  "Delhi")
    cht2.insert("phone", "9999999999")
    cht2.insert("email", "aryan@gmail.com")

    cht2.display()

    # search
    print("\nSearching:")
    print("-" * 40)
    cht2.search("name")
    cht2.search("city")
    cht2.search("country")

    # update existing key
    print("\nUpdating:")
    print("-" * 40)
    cht2.insert("city", "Mumbai")    # update existing key
    cht2.search("city")

    # delete
    print("\nDeleting:")
    print("-" * 40)
    cht2.delete("age")
    cht2.display()

    # ── Example 3: Collision Demo ─────────────
    print("\n" + "=" * 45)
    print("    Collision Demo (size=3)")
    print("    All keys map to same index")
    print("=" * 45)

    cht3 = Chaining_Technique_HashTable(size=3)
    print("\nInserting 3,6,9,12 (all → index 0):")
    print("-" * 40)
    for k in [3, 6, 9, 12]:
        cht3.insert(k)

    cht3.display()