# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.searchTree(root,1)

    def searchTree(self, node,level):
        if node.left == None and node.right == None:
            return level

        if node.left and node.right:
            return min(self.searchTree(node.left,level+1), self.searchTree(node.right,level+1))
        elif node.left:
            return self.searchTree(node.left,level+1)
        else:
            return self.searchTree(node.right,level+1)


        
        
