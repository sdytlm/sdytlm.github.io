# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ret = []
        stack = []
        if root == None:
            return ret
        stack.append(root)
        while stack:
            top = stack.pop()
            ret.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return ret[::-1]
        
