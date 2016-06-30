class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i in range(len(nums)):
            xor ^= i
            xor ^= nums[i]
        # because there is one missing
        return xor^len(nums)
