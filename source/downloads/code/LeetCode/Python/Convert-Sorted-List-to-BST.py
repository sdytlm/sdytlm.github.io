# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        root = TreeNode(-1)
        # find list length
        l = 0
        tmp = head
        while tmp!=None:
            l += 1
            tmp = tmp.next

        root = self.dfs(head,0,l-1)
        return root

    def dfs(self,head,start,end):
        if end<start:
            return None
        mid = (start+end)/2
        tmp = head
        i = 0
        while i < mid:
            i += 1
            tmp = tmp.next
        root = TreeNode(tmp.val)
        root.left = self.dfs(head,start,mid-1)
        root.right = self.dfs(tmp.next,0,end-mid-1)
        return root
