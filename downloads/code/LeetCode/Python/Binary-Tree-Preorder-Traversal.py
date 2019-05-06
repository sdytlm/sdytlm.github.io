# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ret = []
        self.searchTree(root,ret)
        return ret
        
    def searchTree(self, root, ret):
        if root == None:
            return
        ret.append(root.val)
        if root.left != None:
            self.searchTree(root.left,ret)
        if root.right!=None:
            self.searchTree(root.right,ret)
        return
