 class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index_zero = 0
        index_Nzero = 0
        while index_Nzero < len(nums) and index_zero < len(nums):
            # find zero pos
            while index_zero < len(nums) and nums[index_zero] != 0:
                index_zero += 1
            
            if index_zero == len(nums):
                return
            
            # find non-zero pos after zero pos
            index_Nzero = index_zero+1
            while index_Nzero < len(nums) and nums[index_Nzero] == 0:
                index_Nzero += 1
            
            if index_Nzero == len(nums):
                return
            
            nums[index_Nzero],nums[index_zero] = nums[index_zero],nums[index_Nzero]
        return       
