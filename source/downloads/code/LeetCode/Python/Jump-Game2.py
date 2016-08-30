class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        last = 0
        cur = 0
        ret = 0

        for i in range(len(nums)):
            if i > last:
                last = cur
                ret += 1
            cur = max(cur, nums[i] + i)
        return ret
        
