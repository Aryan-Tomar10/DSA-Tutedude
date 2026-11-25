class TreeNode:
    def __init__(self,data):
        self.lchild = None
        self.data = data
        self.rchild = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        self.post_index = 0
    
    def creation_using_postorder(self,postorder,inorder,in_start,in_end):
        if in_start > in_end:
            return None

        root_data = postorder[self.post_index]
        self.post_index -= 1
        node = TreeNode(root_data)

        if in_start==in_end:
            return node
        
        in_idx = self.search(inorder,in_start,in_end,root_data)

        node.lchild = self.creation_using_postorder(postorder,inorder,in_start,in_idx-1)

        node.rchild = self.creation_using_postorder(postorder,inorder,in_idx+1,in_end)

        return node
    
    def search(self,inorder,start,end,key):
        for i in range(start,end+1):
            if inorder[i]==key:
                return i
        return -1
    
    def BuildTree(self,postorder,inorder):
        self.post_index = len(postorder)-1

        self.root = self.creation_using_postorder(postorder, inorder, 0, len(inorder)-1)

    def _preorder(self,p):
        if p:
            self._preorder(p.lchild)
            print(p.data,end = " , ")
            self._preorder(p.rchild)
    
    def preorder(self):
        self._preorder(self.root)

if __name__ == "__main__":
    BST = Binary_Search_Tree()
    postorder = [30,20,10,15,25]
    inorder = sorted(postorder)
    BST.BuildTree(postorder,inorder)
    
    print("\nPreorder : ",end = " ")
    BST.preorder()
    print()