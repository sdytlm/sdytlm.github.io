# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # find lenA and lenB
        lenA = self.getsize(headA)
        lenB = self.getsize(headB)


        # find intersection
        if lenA<lenB:
            return self.getIntersectionNode(headB,headA)
        
        for i in range(lenA-lenB):
            headA = headA.next

        while headA and headB:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
    def getsize(self, node):
        len = 0
        while node:
            len += 1
            node = node.next
        return len

