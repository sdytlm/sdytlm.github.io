 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        stack = []
        node = root
        # pre-order tranversal
        self.pre_order(stack,root)
        
        stack.pop(0)
        # change tree
        while stack:
            node.right = stack.pop(0)
            node.left = None
            node = node.right


    def pre_order(self,stack,root):
        if root == None:
            return
        stack.append(root)
        self.pre_order(stack,root.left)
        self.pre_order(stack,root.right)
       
