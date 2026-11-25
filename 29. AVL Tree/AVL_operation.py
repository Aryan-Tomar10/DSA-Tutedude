class TreeNode:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def _height(self,node):
        if node is None:
            return 0
        return node.height
    
    def height(self):
        return self._height(self.root)
    
    def _balance_factor(self,node):
        if node is None:
            return 0
        return self._height(node.lchild)-self._height(node.rchild)
    
    def _update_height(self,node):
        if node:
            node.height = 1+max(self._height(node.lchild),self._height(node.rchild))
        
    def _balance(self,node):
        self._update_height(node)
        bf = self._balance_factor(node)

        #LL case
        if bf>1 and self._balance_factor(node.lchild)>=0:
            return self._rotate_right(node)
        
        #LR case
        if bf>1 and self._balance_factor(node.lchild)<0:
            node.lchild = self._rotate_left(node.lchild)
            return self._rotate_right(node)
        
        #RR case
        if bf<-1 and self._balance_factor(node.rchild)<=0:
            return self._rotate_left(node)
        
        #RL case
        if bf<-1 and self._balance_factor(node.rchild)>0:
            node.rchild = self._rotate_right(node.rchild)
            return self._rotate_left(node)
        
        return node
    
    #ROTATION
    # ── Right Rotation (LL Case) ───────────────
    #
    #       z                y
    #      / \             /   \
    #     y   T4          x     z
    #    / \      →      / \   / \
    #   x   T3          T1 T2 T3 T4
    #  / \
    # T1  T2
    #
    def _rotate_right(self,z):
        y=z.lchild
        T3 = y.rchild

        y.rchild =  z
        z.lchild = T3

        self._update_height(z)
        self._update_height(y)

        return y

    # ── Left Rotation (RR Case) ────────────────
    #
    #     z                  y
    #    / \               /   \
    #   T1   y            z     x
    #       / \   →      / \   / \
    #      T2  x        T1 T2 T3 T4
    #         / \
    #        T3  T4
    #

    def _rotate_left(self,z):
        y = z.rchild
        T2 = y.lchild

        y.lchild = z
        z.rchild = T2

        self._update_height(z)
        self._update_height(y)

        return y
    
    # INSERTION    
    def _insert(self,root,key):
        if root is None:
            return TreeNode(key)
        if key<root.data:
            root.lchild = self._insert(root.lchild,key)
        elif key>root.data:
            root.rchild = self._insert(root.rchild,key)
        else:
            print(f"{key} already exist.")
            return root
        return self._balance(root)
    
    def insert(self,key):
        self.root = self._insert(self.root,key)
    

    #TRAVERSAL
    def _inorder(self,p):
        if p:
            self._inorder(p.lchild)
            print(p.data, end = ",")
            self._inorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)
            
    def _preorder(self,p):
        if p:
            print(p.data, end = ",")
            self._preorder(p.lchild)
            self._preorder(p.rchild)

    def preorder(self):
        self._preorder(self.root)

    def _postorder(self,p):
        if p:
            self._postorder(p.lchild)
            self._postorder(p.rchild)
            print(p.data, end = ",")
    
    def postorder(self):
        self._postorder(self.root)

    def Min_node(self,node):
        while node.lchild:
            node = node.lchild
        return node

    def _delete(self,root,key):
        if root is None:
            return None
        if key<root.data:
            root.lchild = self._delete(root.lchild,key)
        elif key>root.data:
            root.rchild = self._delete(root.rchild,key)
        else:
            if root.lchild is None:
                return root.rchild
            elif root.rchild is None:
                return root.lchild
            else:
                successor = self.Min_node(root.rchild)
                root.data = successor.data
                root.rchild = self._delete(root.rchild,successor.data)
        return self._balance(root)
    
if __name__ == '__main__':
    AVL = AVLTree()
    AVL.insert(10)
    AVL.insert(20)
    AVL.insert(30)
    AVL.insert(25)
    AVL.insert(28)
    AVL.insert(27)
    AVL.insert(5)

    print("inorder Traversal is ", end="")
    AVL.inorder()
    print()
    print(f"Height : {AVL.height()}")