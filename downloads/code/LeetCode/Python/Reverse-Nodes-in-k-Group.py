# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(l):
            newEnd = l
            tmp = l.next
            while tmp != None:
                n = tmp.next
                tmp.next = l
                l = tmp
                tmp = n
            newEnd.next = None
            # 需要返回newEnd,就是下一个节点的prev
            return [l,newEnd]


        def findEnd(start,k):
            i = 1
            ret = start
            while i < k and ret != None:
                i += 1
                ret = ret.next
            return ret

        newNode = ListNode(-1)
        newNode.next = head

        prev = newNode
        start = head

        while start!= None and start.next != None:
            end = findEnd(start,k)
            if end == None:
                return newNode.next
            nextNode = end.next
            end.next = None

            ret= reverse(start)
            # 把 reversed substring 和现有的连起来
            prev.next = ret[0]
            ret[1].next = nextNode
            start = nextNode
            prev = ret[1]
        return newNode.next
