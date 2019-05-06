# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newHead = ListNode(-1)
        newHead.next = head

        # get length
        length = 0
        while head != None:
            head=head.next
            length += 1

        head = newHead
        i = 0
        while i < length-n:
            i += 1
            head = head.next

        head.next = head.next.next
        return newHead.next
        
