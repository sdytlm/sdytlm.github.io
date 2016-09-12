class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        
        
        up = [1]*n
        down = [1] * n

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                up[i] = up[i-1]
                down[i] = down[i-1]
            # wiggle down, we need to find the length of last wiggle up
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            # wiggle up, we need to find the length of last wiggle down
            else:
                up[i] = down[i-1]+1
                down[i] = down[i-1]
        return max(max(up),max(down))

