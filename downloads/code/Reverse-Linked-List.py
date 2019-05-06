# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        prev = ListNode(-1)
        prev.next = head

        node = head

        while node:
            nextnode = node.next
            if node == head:
                node.next = None
            else:
                node.next = prev
            prev = node
            node = nextnode
        return prev
            
