# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # heap[i] : (node, node.val)
        heap = []

        for root in lists:
            if root:
                heapq.heappush(heap,(root.val, root))

        head = ListNode(-1)
        ret = head
        while heap:
            smallestNode = heapq.heappop(heap)[1]
            head.next = smallestNode
            head = head.next
            if smallestNode.next:
                heapq.heappush(heap,(smallestNode.next.val, smallestNode.next))
        return ret.next
