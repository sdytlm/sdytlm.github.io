# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object): 
    def rotateRight(self, head, k): 
        if head == None or head.next == None:
            return head
        l = 1 
        i = 0 
        tmp = head 
        # Get the length 
        while tmp.next != None: 
            l += 1 
            tmp = tmp.next 
        dummy_node = ListNode(-1) 
        dummy_node.next = head 
        k = k%l 
        if k == 0: 
            return head 
        while i<l-k: 
            dummy_node = dummy_node.next
            i += 1
        newhead = dummy_node.next 
        dummy_node.next = None 
        # connect the old head to new head 
        tmp = newhead
        while tmp.next != None:
            tmp = tmp.next     
        tmp.next = head
        return newhead
