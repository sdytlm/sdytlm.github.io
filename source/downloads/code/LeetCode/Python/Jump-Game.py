class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #index_true: current reachable index.
        if not nums or len(nums) == 0:
            return False

        index_true = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i >= index_true:
                index_true = i
        if index_true == 0:
            return True
        else:
            return False
        
