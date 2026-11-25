class TreeNode:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = None
        self.post_idx = 0
    
    def _build(self,postorder,inorder,in_start, in_end):
        if in_start>in_end:
            return None

        root_data = postorder[self.post_idx]
        self.post_idx-=1
        node = TreeNode(root_data)

        if in_start == in_end:
            return node

        in_idx = self._search(inorder,in_start,in_end,root_data)

        node.lchild = self._build(postorder, inorder, in_start,in_idx-1)

        node.rchild = self._build(postorder, inorder, in_idx+1,in_end)

        return node
    
    def _search(self,inorder,start,end,key):
        for i in range(start,end+1):
            if inorder[i]==key:
                return i
        return -1
    
    def BuildTree(self,postorder,inorder):
        self.post_idx = len(postorder) - 1
        self.root = self._build(postorder, inorder, 0, len(inorder) - 1)
    
    def _preorder(self,p):
        if p:
            print(p.data,end = " , ")
            self._preorder(p.lchild)
            self._preorder(p.rchild)

    def preorder(self):
        self._preorder(self.root)
    
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
    postorder = [4,5,2,6,7,3,1]
    inorder = [4,2,5,1,6,3,7]
    bt.BuildTree(postorder,inorder)
    
    print("\nPretorder : ",end = " ")
    bt.preorder()

    print()

    print("Height of Tree is : ",bt.height())

    print("Total number of node are : ",bt.count())