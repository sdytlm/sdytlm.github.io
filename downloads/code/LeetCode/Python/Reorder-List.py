#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return 
        # split the list
        prevNode = ListNode(-1)
        prevNode.next = head
        slow = prevNode
        fast = prevNode

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = head

        # reverse the right
        prev = right
        nextNode = right.next
        prev.next = None
        while nextNode!=None:
            tmp = nextNode.next
            nextNode.next = prev
            prev = nextNode
            nextNode = tmp

        right = prev

        # Merge the list
        while right != None:
            leftNext = left.next
            rightNext = right.next
            left.next = right
            right.next = leftNext
            left = leftNext
            right = rightNext

