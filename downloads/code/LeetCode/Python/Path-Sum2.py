# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findPath(self,result,vector,node,bal):
        vector.append(node.val)
        if node.val == bal and node.left == None and node.right == None:
            result.append(vector[:])
            return

        if node.left != None:
            self.findPath(result,vector,node.left,bal-node.val)
            vector.pop()
        if node.right != None:
            self.findPath(result,vector,node.right,bal-node.val)
            vector.pop()
        return




    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
    
        result = []
        vector = []
        if root == None:
            return result

        self.findPath(result,vector,root,sum);
        return result
