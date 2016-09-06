# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head == None:
            return head
        # hash_table: <old_node, new_node>
        hash_table = dict()
        dummy = RandomListNode(0)
        newHead = dummy
        node = head
        # 链接next
        while node:
            newNode = RandomListNode(node.label)
            newHead.next = newNode
            hash_table[node] = newNode

            node = node.next
            newNode = newNode.next

        node = head
        newHead = dummy.next

        # 链接random
        while node:
            if node.random:
                newHead.random = hash_table[node.random]
            
            node = node.next
            newHead = newHead.next
        return dummy.next
