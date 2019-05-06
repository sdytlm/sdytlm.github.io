class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        ret = 0
        i = 0
        index = 1
        while i < len(nums):
            ret += 1
            j = i+1
            while j<len(nums) and nums[i] == nums[j]:
                j = j+1
            
            if j < len(nums):
                nums[index] = nums[j]
                index += 1
            i = j
        return ret
