# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        i = 0
        ans = 0
        head = self.head
        while head:
            # randint 是在[0,i]中生成随机数
            # roll到0才算数
            if random.randint(0,i) == 0:
                ans = head.val
            # head 一直在前进
            head = head.next
            i = i+
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
