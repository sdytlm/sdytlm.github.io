# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next==None:
            return head

        # merge sort
        fast_node = head
        slow_node = head

        # find pivot
        while fast_node.next != None and fast_node.next.next != None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        middle = slow_node.next
        slow_node.next = None
        
        # split
        leftNode = self.sortList(head)
        rightNode = self.sortList(middle)

        return self.merge(leftNode,rightNode)

    # merge
    def merge(self,left,right):
        if left != None and right == None:
            return left
        if left == None and right != None:
            return right
        if left == None and righ == None:
            return None
        
        # find head 
        ret = None
        if left.val < right.val:
            ret = left
            left = left.next
        else:
            ret = right
            right = right.next
        
        # merge every node
        head = ret
        while left != None and right != None:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        
        if left != None:
            head.next = left
        if right != None:
            head.next = right
       
        return ret

