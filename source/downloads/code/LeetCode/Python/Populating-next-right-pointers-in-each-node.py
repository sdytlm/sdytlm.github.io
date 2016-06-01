# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        queue = []
        queue.append((root,0))
        oldnode = root
        oldlevel = 0
        while queue:
            item = queue.pop(0)
            cur = item[0]
            level = item[1]
            if cur.left != None:
                queue.append((cur.left,level+1))
            if cur.right != None:
                queue.append((cur.right,level+1))
            
            if oldnode != cur and oldlevel == level:
                oldnode.next = cur
            oldlevel = level
            oldnode = cur
        return
