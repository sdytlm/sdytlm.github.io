# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        lh = 0
        rh = 0
        tmp = root
        
        # find 极左子树的高度
        while tmp:
            lh += 1
            tmp = tmp.left
    
        # find 极右子树的高度

        tmp = root
        while tmp:
            rh += 1
            tmp = tmp.right

        if lh == rh:
            return 2**lh -1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
