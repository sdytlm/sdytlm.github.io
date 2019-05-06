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

        def connectNode(prev,node):
            # 有可能送进来的是第一个节点
            if prev != None:
                prev.next = node


        if root == None:
            return None

        parent = root
        root.next = None
        while parent:
            # 每一行第一个节点
            firstNode = None
            # 上一次链接的节点
            lastNode = None
            # 循环一次可以把一整行的节点的字节点连接好
            while parent is not None:
                for node in [parent.left,parent.right]:
                    if node == None:
                        continue
                    # 当拿到右边节点的时候才会链接
                    connectNode(lastNode,node)
                    # 碰到了每一行的第一个节点
                    if lastNode == None:
                        firstNode = node

                    lastNode = node
                parent = parent.next
            parent = firstNode
                
            
