class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e = 0
        counter = 0
        for x in nums:
            if counter == 0:
                e = x
                counter += 1
            elif e == x:
                counter += 1
            else:
                counter -= 1
        return e
