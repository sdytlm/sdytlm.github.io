class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        n = len(nums)
        dp = [0]*(n)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])

        # case1: dont use dp[0]
        dp[0] = 0
        dp[1] = nums[1]

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        ans = dp[n-1]

        # case2: don't use dp[n-1]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n-1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        return max(ans,dp[n-2])
