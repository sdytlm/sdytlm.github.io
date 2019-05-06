# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret

        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left

        while stack:
            node = stack.pop()
            ret.append(node.val)
            # push the left subtree of right child
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return ret

if __name__ == "__main__":
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    print sol.inorderTraversal(node1)
