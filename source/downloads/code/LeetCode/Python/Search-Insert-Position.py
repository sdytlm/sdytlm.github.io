class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if nums[0] >= target:
            return 0

        for i in range(1,len(nums)):
            if nums[i] == target:
                return i
            if target < nums[i]:
                return i
        return len(nums)
