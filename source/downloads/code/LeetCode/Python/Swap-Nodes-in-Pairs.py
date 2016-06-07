# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        front = head
        end = front.next
        prev = ListNode(-1)
        prev.next = head
        newhead = head.next
        
        while end!=None:
            nextNode = end.next
            front.next = nextNode
            end.next = front
            prev.next = end
            
            if nextNode == None:
                break
            prev = front
            front = nextNode
            end = front.next

        return newhead
