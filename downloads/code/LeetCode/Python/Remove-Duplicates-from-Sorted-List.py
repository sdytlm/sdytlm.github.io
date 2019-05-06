# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
	newHead = ListNode(0)
        newHead.next = head
        ret = newHead

        newHead = head
        head = head.next

        while head != None:
            if head.val != newHead.val:
                newHead.next = head
                newHead = head
            head = head.next
        newHead.next = None
        return ret

