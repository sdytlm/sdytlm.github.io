class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)== 0:
            return None

        root = TreeNode(postorder[-1])
        indexInorder = inorder.index(postorder[-1])

        root.right = self.buildTree(inorder[indexInorder+1:],postorder[indexInorder:-1])
        root.left = self.buildTree(inorder[:indexInorder],postorder[:indexInorder] )
        return root

### The above code will cause out of memory error

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
  
class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder: return None # inorder is empty
        self.inorder, self.postorder = inorder, postorder
        return self.dfs(0, 0, len(inorder))
     
    def dfs(self, inLeft, postLeft, Len):
        if Len <= 0:
            return None
        root = TreeNode(self.postorder[postLeft + Len - 1])
        rootPos = self.inorder.index(self.postorder[postLeft + Len - 1])
        root.left = self.dfs(inLeft, postLeft, rootPos - inLeft)
        root.right = self.dfs(rootPos + 1, postLeft + rootPos - inLeft, Len - 1 - (rootPos - inLeft))
        return root
