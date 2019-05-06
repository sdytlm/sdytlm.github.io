class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        r = len(nums)-1
        l = 0

        while l <= r:
            # 从右往左找到不是val的地方
            while l <=r and nums[r] == val:
                r -= 1
            
            if l > r:
                return l
            
            # 把val挪到r的位置
            if nums[l] == val:
                nums[l],nums[r] = nums[r],nums[l]
            
            l += 1
        return l
