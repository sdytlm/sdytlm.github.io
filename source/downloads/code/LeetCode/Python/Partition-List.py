#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        right = ListNode(-1)
        newhead = ListNode(-1)
        left_head = newhead
        right_head = right
        # assign the nodes into two lists
        while head != None:
            newNode = ListNode(head.val)
            if head.val < x:
                left_head.next = newNode
                left_head = left_head.next
            if head.val >= x:
                right_head.next = newNode
                right_head = right_head.next
            head = head.next
        # connect two lists
        left_head.next = right.next
        return newhead.next
            
