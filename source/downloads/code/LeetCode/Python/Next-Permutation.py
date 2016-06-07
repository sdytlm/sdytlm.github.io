class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        # find the element after which the elements are descending
        k = len(nums)-2
        while k>=0:
            if nums[k] < nums[k+1]:
                break
            k -= 1
        
        # 5 4 3 2 1
        if k < 0:
            nums.sort()
            return

        # find the smallest nums[l] > nums[k]
        l = len(nums)-1
        while l>k:
            if nums[l] > nums[k]:
                break
            l -= 1
        nums[k],nums[l] = nums[l],nums[k]

        nums[:] = nums[:k+1] + nums[:k:-1]
