# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True

        dummy = ListNode(-1)
        dummy.next = head
        # find the mid
        slow = dummy
        fast = dummy

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # reverse the right half
        start = mid
        end = mid.next
        start.next = None
        while end != None:
            tmp = end.next
            end.next = start
            start = end
            end = tmp
        
        # compare the left half and right half
        right_head = start
        left_head = head
        
        while right_head != None and left_head != None:
            if right_head.val != left_head.val:
                return False
            right_head = right_head.next
            left_head = left_head.next
        return True

