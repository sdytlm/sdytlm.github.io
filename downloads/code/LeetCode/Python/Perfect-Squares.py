import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i+j*j] = min(dp[i]+1, dp[i+j*j])

        dp = [sys.maxint]*(n+1)
        i = 1
        while i*i <= n:
            dp[i*i] = 1
            i += 1
        for i in range(1,n+1):
            j = 1
            while i+j*j <=n:
                dp[i+j*j] = min(dp[i]+1, dp[i+j*j])
                j += 1
        return dp[n]
if __name__ == "__main__":
    sol = Solution()
    print sol.numSquares(5673)
