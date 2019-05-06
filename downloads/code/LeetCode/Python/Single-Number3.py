class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # calculate the xor for all nums
        xor = 0
        result = [0,0]
        for i in nums:
            xor ^= i
        # get the low bit
        lowbit = xor & -xor

        # get the result
        for i in nums:
            if lowbit & i == 0:
                result[0] ^= i
            else:
                result[1] ^= i
        return result

        
