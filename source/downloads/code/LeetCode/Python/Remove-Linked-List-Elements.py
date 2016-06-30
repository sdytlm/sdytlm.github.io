# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # [1,1], 1
    # [1],2
    # [1],1
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        prev = ListNode(-1)
        prev.next = head
        cur = head
        newhead = prev

        while cur!=None:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
                continue
            prev = prev.next
            cur = cur.next
        return newhead.next
        
