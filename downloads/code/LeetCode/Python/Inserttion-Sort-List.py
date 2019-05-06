# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        new_node = ListNode(-sys.maxint-1)
        # new_node.next = head
        new_node.next = head
        head = new_node
        # tail: biggest element current sorted list
        tail = head
        
        
        while tail.next:
            
            cur = tail.next
            # case: just assign new node after the tail
            if cur.val >= tail.val:
                tail = tail.next
            else: # case: need to insert the node again
                # find the place
                prev = head
                new_cur = prev.next
                while new_cur.val < cur.val:
                    new_cur = new_cur.next
                    prev = prev.next
                # remove the node
                tail.next = cur.next
                # insert the node again
                cur.next = prev.next
                prev.next = cur
                
        return head.next
                                                                                                                                                                                                                                                                                                           return head.
