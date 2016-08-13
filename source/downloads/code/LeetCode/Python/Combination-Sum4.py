class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(target+1):
            for j in nums:
                if i+j <= target:
                    dp[i+j] += dp[i]
        return dp[target]
