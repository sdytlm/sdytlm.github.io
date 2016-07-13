# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        # push the most left nodes
        node = root
        while node:
            stack.append(node)
            node = node.left
        while stack and k>0:
            node = stack.pop()
            k = k-1
            # push the left subtree of the node.right
            rightChild = node.right
            while rightChild:
                stack.append(rightChild)
                rightChild = rightChild.left
        return node.val 
