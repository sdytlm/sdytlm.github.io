# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rec(self,leftNode,rightNode):
        if leftNode == None and rightNode == None:
            return True
        if leftNode == None and rightNode != None:
            return False
        if leftNode != None and rightNode == None:
            return False
        if leftNode.val != rightNode.val:
            return False
    
        return self.rec(leftNode.left, rightNode.right) and self.rec(leftNode.right, rightNode.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        return self.rec(root.left, root.right)
        
