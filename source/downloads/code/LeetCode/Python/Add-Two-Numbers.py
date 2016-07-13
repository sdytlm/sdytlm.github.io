# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        addon=0
        ret = ListNode(-1)
        node = ret
        while l1 or l2:
            newval = 0
            if l1 and l2:
                newval = l1.val + l2.val + addon
            elif l1:
                newval = l1.val + addon
            else:
                newval = l2.val + addon
            newNode = ListNode(newval%10)
            node.next = newNode
            node = newNode
            addon = newval / 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if addon == 1:
            node.next = ListNode(1)
        return ret.next
