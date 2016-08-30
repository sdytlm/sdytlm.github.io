class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums)-1
        if len(nums) == 0:
            return False

        while l <= r:
            # skip duplicates
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r] == nums[r-1]:
                r -= 1

            m = (l+r)/2
            if nums[m] == target:
                return True
            if nums[m] >= nums[l]:
                if nums[l] <= target and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False
                                                            
