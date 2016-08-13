# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        n = len(preorder)
        if n == 0:
            return None

        root = TreeNode(preorder[0])
        indexIn = inorder.index(preorder[0])
        leftL = indexIn
        root.left = self.buildTree(preorder[1:(1+leftL)], inorder[0:indexIn])
        root.right = self.buildTree(preorder[1+leftL:], inorder[indexIn+1,:])

        return root
        
