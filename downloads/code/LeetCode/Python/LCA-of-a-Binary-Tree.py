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
        # 访问树底或者发现目标节点
        if root == None or root == p or root == q:
            return root
        leftTree = self.lowestCommonAncestor(root.left,p,q)
        rightTree = self.lowestCommonAncestor(root.right,p,q)
        
        # 这个root刚好左右子树各有一个目标节点
        if leftTree != None and rightTree != None:
            return root
        # 只有左子树有目标
        if leftTree != None:
            return leftTree
        else:
            # 只有右子树有目标
            return rightTree
