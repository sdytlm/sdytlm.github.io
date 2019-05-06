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
        node = ListNode(-1)
        ret = node
        while head != None:
            nextNode = head.next
            # find next node
            if nextNode != None and nextNode.val == head.val:
                while nextNode != None and nextNode.val == head.val:
                    nextNode = nextNode.next
            else:
                # found non-duplicated nodes
                node.next = head
                node = head
                # in case there is no other node
                node.next = None

            head = nextNode
        return ret.next      
