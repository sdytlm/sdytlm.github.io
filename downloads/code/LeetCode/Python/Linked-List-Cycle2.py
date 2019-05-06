# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None

        slow = head
        fast = head

        while fast.next!=None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if fast.next == None or fast.next.next==None:
            return None

        # find the start point
        a = head
        while a != fast:
            a = a.next
            fast = fast.next
        return a
