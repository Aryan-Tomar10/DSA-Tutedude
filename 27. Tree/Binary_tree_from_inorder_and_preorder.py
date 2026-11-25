class TreeNode:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = None
        self.pre_index = 0
    
    def _build(self, preorder, inorder, in_start, in_end):
        if in_start>in_end:
            return None
        root_data = preorder[self.pre_index]
        self.pre_index+=1
        node = TreeNode(root_data)

        if in_start == in_end:
            return node
        
        in_idx = self.search(inorder,in_start,in_end,root_data)

        node.lchild = self._build(preorder, inorder, in_start, in_idx-1)

        node.rchild = self._build(preorder, inorder, in_idx+1, in_end)

        return node
        
    def search(self, inorder, start, end, key):
        for i in range(start,end+1):
            if inorder[i] == key:
                return i
        return -1


    def BuildTree(self,preorder,inorder):
        self.pre_index = 0

        self.root = self._build(preorder, inorder, 0, len(inorder)-1)

    def _postorder(self,p):
        if p:
            self._postorder(p.lchild)
            self._postorder(p.rchild)
            print(p.data,end = " , ")
    
    def postorder(self):
        self._postorder(self.root)

if __name__ == "__main__":
    bt = Tree()
    preorder = [1,2,4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7]
    bt.BuildTree(preorder,inorder)
    
    print("\nPostorder : ",end = " ")
    bt.postorder()
    print()