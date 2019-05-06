# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # DFS
    # return: 抢劫node的收益， 不抢劫node的受益
    def dfs(self,node):
        if node == None:
            return 0,0
        rob_L, no_rob_L = self.dfs(node.left)
        rob_R, no_rob_R = self.dfs(node.right)
        return no_rob_L+no_rob_R+node.val, max(no_rob_R,rob_R) + max(no_rob_L, rob_L)
    

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ret = self.dfs(root)
        return max(ret[0],ret[1])
