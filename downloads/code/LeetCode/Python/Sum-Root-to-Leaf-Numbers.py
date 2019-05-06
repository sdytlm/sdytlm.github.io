# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        val = []
        self.findVal(val,root,0)
        ret = 0
        for i in val:
            ret += i
        return ret

    def findVal(self,val,root,tmp):
        if root == None:
            return
        
        tmp = tmp*10 + root.val
        if root.left == None and root.right == None:
            val.append(tmp)
            return
        
        self.findVal(val,root.left,tmp)
        self.findVal(val,root.right,tmp)
        return
