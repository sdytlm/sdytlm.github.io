class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums:
            return 0
        # 把[1]分别插入首和尾
        nums = [1] + nums + [1]
        dp = [[0] * (n+2) for x in range(n+2)]
        
        def DP(i,j):
            if dp[i][j] > 0:
                return dp[i][j]
            for x in range(i,j+1):
                dp[i][j] = max(dp[i][j], DP(i,x-1)+nums[i-1]*nums[x]*nums[j+1] + DP(x+1,j))
            return dp[i][j]
        return DP(1,n)
