class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        if len(nums) == 0:
            return -1

        while l <= r:
            m = (l+r)/2
            if nums[m] == target:
                return m
            # m左面递增
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            # m右边递增
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1
