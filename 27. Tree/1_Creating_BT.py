from collections import deque

class Node:
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
        self.root = Node(x)
        q.append(self.root)
        while(q):
            p = q.popleft()
            x = int(input(f"Enter the Left child data {p.data} : "))
            if(x!=-1):
                t = Node(x)
                p.lchild = t
                q.append(t)
            x = int(input(f"Enter the Right child data {p.data} : "))
            if(x!=-1):
                t = Node(x)
                p.rchild = t
                q.append(t)

    def _inorder(self,p):
        if p:
            self._inorder(p.lchild)
            print(p.data, end=" , ")
            self._inorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)

    def _preorder(self,p):
        if p:
            print(p.data, end=" , ")
            self._preorder(p.lchild)
            self._preorder(p.rchild)

    def preorder(self):
        self._preorder(self.root)
    
    def _postorder(self,p):
        if p:
            self._postorder(p.lchild)
            self._postorder(p.rchild)
            print(p.data, end=" , ")

    def postorder(self):
        self._postorder(self.root)

    def leveOrder(self):
        if not self.root:
            print("Tree is empty")
            return
        q = deque()
        q.append(self.root)
        while q:
            curr = q.popleft()
            print(curr.data,end = " , ")
            if curr.lchild:
                q.append(curr.lchild)
            if curr.rchild:
                q.append(curr.rchild)
        print()

if __name__ == "__main__":
    bt = Tree()
    bt.Creating_Tree()
    print("\nInorder : ",end = " ")
    bt.inorder()
    print("\nPreorder : ",end = " ")
    bt.preorder()
    print("\nPostorder : ",end = " ")
    bt.postorder()
    print()
    print("\nLevel order : ",end = " ")
    bt.leveOrder()
    print()