# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

       
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        dummy.next = head

        #找到m-1
        mth_prev = self.findNode(dummy,m-1)
        mth = mth_prev.next
        
        # 找到n
        nth = self.findNode(dummy,n)
        nth_next = nth.next
        nth.next = None

        #revert <m,n>
        self.revert(mth)
        mth_prev.next = nth
        mth.next = nth_next
        return dummy.next

    def findNode(self,head,k):
        i = 0
        while i<k:
            if head == None:
                return None
            head = head.next
            i += 1
        return head

    def revert(self, head):
        prev = None
        while head!=None:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev


