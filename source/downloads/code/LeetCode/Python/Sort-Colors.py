class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return

        indexR = 0
        indexB = len(nums)-1

        i = 0
        while i <= indexB:
            if nums[i] == 0:
                nums[indexR],nums[i] = nums[i],nums[indexR]
                indexR += 1
                i += 1
            elif nums[i] == 2:
                nums[indexB],nums[i] = nums[i],nums[indexB]
                indexB -= 1
            else:
                i += 1
