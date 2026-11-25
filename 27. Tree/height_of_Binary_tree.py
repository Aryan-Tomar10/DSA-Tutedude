from collections import deque

class TreeNode:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = None

    def Creating_Tree(self):
        q = deque()
        x = int(input("Enter the root data : "))
        if x==-1:
            return 0
        self.root = TreeNode(x)
        q.append(self.root)
        while(q):
            p = q.popleft()
            x = int(input(f"Enter the Left child data {p.data} : "))
            if(x!=-1):
                t = TreeNode(x)
                p.lchild = t
                q.append(t)
            x = int(input(f"Enter the Right child data {p.data} : "))
            if(x!=-1):
                t = TreeNode(x)
                p.rchild = t
                q.append(t)
    
    def _height(self,p):
        l,r = 0,0
        if p:
            l = self._height(p.lchild)
            r = self._height(p.rchild)
            if l>r:
                return l+1
            else:
                return r+1
        return 0
    
    def height(self):
        return self._height(self.root)

    def _count(self,p):
        l,r = 0,0
        if p:
            l = self._count(p.lchild)
            r = self._count(p.rchild)
            return l+r+1
        return 0
    
    def count(self):
        return self._count(self.root)

if __name__ == "__main__":
    bt = Tree()
    
    bt.Creating_Tree()
    
    print("\nHeight of Binary Tree is : ",bt.height())
    
    print("\nTotal number of Node in Binary Tree is : ",bt.count())

    print()