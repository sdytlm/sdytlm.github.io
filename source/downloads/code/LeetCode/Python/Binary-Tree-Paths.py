# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
   
    def dfs(self,ret,path,node):
        path += str(node.val)
        if node.left == None and node.right == None:
            ret.append(path[:])
        path += "->"
        if node.left != None:
            self.dfs(ret,path,node.left)
        if node.right != None:
            self.dfs(ret,path,node.right)


    def binaryTreePaths(self, root):
        ret = []
        if root == None:
            return ret
        self.dfs(ret,"",root)
        return ret
