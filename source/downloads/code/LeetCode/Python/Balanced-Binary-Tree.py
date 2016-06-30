# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # should have two return value <balanced, height>
    # judge start from the bottom 
    def valid(self, node):
        if node == None:
            return True,0
        balanced, lh = self.valid(node.left)
        if balanced == False:
            return False,0
        balanced, rh = self.valid(node.right)
        if balanced == False:
            return False,0

        return abs(lh-rh)<=1, max(lh,rh)+1


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balanced, height = self.valid(root)
        return balanced
