# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1 = None
        self.n2 = None
        self.prev = None

        self.tranverse(root)
        self.n1.val,self.n2.val = self.n2.val, self.n1.val
        return

    def tranverse(self, node):
        if node == None:
            return
        # 中序遍历应该得到递增序列 
        self.tranverse(node.left)
        # 有可能出现１个或２个递减情况
        if self.prev and self.prev.val > node.val:
            self.n2 = node
            if self.n1 == None:
                self.n1 = self.prev
        
        self.prev = node
        self.tranverse(node.right)

