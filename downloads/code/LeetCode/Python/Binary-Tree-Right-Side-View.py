# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        ret = []

        if root == None:
            return ret

        stack.append([root,level])

        while stack:
            top = stack.pop(0)
            node = top[0]
            cur_level = top[1]
            
            if node.left != None:
                stack.append([node.left,cur_level+1])
            if node.right != None:
                stack.append([node.right,cur_level+1])
            
            if not stack or cur_level != stack[0][1]:
                ret.append(node.val)

        return ret
