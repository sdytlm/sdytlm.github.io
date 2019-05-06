# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return None
        # 找到目标之一
        if root.val == p.val or root.val == q.val:
            return root

        leftTree = self.lowestCommonAncestor(root.left,p,q)
        rightTree = self.lowestCommonAncestor(root.right,p,q)

        if leftTree != None and rightTree != None:
            return root
        if leftTree != None:
            return leftTree
        if rightTree != None:
            return rightTree
        return None
