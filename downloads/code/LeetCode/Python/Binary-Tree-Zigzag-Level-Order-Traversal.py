# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        stack = []
        level = 0
        stack.append(root)
        while stack:
            newstack = []
            if level % 2 == 0:
                ret.append([x.val for x in stack])
            else:
                ret.append([stack[x].val for x in range(len(stack)-1,-1,-1)])
            
            for node in stack:
                if node.left:
                    newstack.append(node.left)
                if node.right:
                    newstack.append(node.right)
            level += 1
            stack = newstack
        return ret
