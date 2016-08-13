# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if node == None:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            # 比较leftmax+rightmax+node.val 和self.ans (因为node.val可能是负数)
            self.ans = max(max(leftMax,0)+max(rightMax,0)+node.val, self.ans)
            # 因为leftMax,rightMax可能是负数,我们只要root.val
            return max(leftMax，rightMax,0)+node.val 
        return self.ans        
