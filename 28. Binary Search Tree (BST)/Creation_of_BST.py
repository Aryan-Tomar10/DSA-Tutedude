class TreeNode:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def _insert(self,root,key):
        if root is None:
            return TreeNode(key)
        if key < root.data:
            root.lchild = self._insert(root.lchild,key)
        elif key > root.data:
            root.rchild = self._insert(root.rchild,key)
        else:
            print(f"{key} already exist.")
        return root
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _search(self,root,key):
        if root is None:
            return None
        if key == root.data:
            return root
        elif key<root.data:
            return self._search(root.lchild,key)
        else:
            return self._search(root.rchild,key)
    
    def search(self, key):
        return self._search(self.root, key)
        # result = self._search(self.root, key)
        # if result:
        #     print(f"{key} found in BST")
        # else:
        #     print(f"{key} not found in BST")
    
    def _inorder(self,root):
        if root:
            self._inorder(root.lchild)
            print(root.data,end = " , ")
            self._inorder(root.rchild)

    def inorder(self):
        self._inorder(self.root)

    def delete_BST(self,root,key):
        if root is None:
            return None
        if key < root.data:
            root.lchild = self.delete_BST(root.lchild,key)
        elif key > root.data:
            root.rchild = self.delete_BST(root.rchild,key)
        else:
            if root.lchild is None and root.rchild is None:
                return None
            elif root.lchild is None:
                return root.rchild
            elif root.rchild is None:
                return root.lchild
            else:
                successor = self._min_node(root.rchild)
                root.data = successor.data
                root.rchild = self.delete_BST(root.rchild, successor.data)
        return root
    
    def _min_node(self,node):
        while node.lchild:
            node = node.lchild
        return node

    def delete(self,key):
        self.root = self.delete_BST(self.root,key)

if __name__ == "__main__":
    BST = Binary_Search_Tree()
    x = int(input("Enter the number of nodes to be added : "))

    for i in range(x):
        data = int(input(f"Enter data {i+1} : "))
        BST.insert(data)
    
    data = int(input(f"\nEnter data to be searched : "))
    print(BST.search(data))

    print("\nInorder Traversal : ", end = " ")
    BST.inorder()

    key = int(input("\nEnter the node to be Delete Node : "))
    BST.delete(key)

    print("\nInorder Traversal : ", end = " ")
    BST.inorder()