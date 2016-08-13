# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            node = ListNode(-1)
            root = node
            while l1 and l2:
                if l1.val <= l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            if l1 != None:
                node.next = l1
            if l2 != None:
                node.next = l2
        return root.next
