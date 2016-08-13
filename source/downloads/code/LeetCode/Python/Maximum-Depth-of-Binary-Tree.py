# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root,0)

    def dfs(self,root,cur):
        if root == None:
            return cur
        depth = max(self.dfs(root.left,cur+1), self.dfs(root.right,cur+1))
        return depth
