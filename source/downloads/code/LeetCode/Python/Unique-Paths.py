class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m<=0 or n <=0:
            return 0

        dp = [[0] * (n+1) for i in range(m+1)]
        # make the first row as 1
        for i in range(n+1):
            dp[1][i] = 1
        # dp starts from the second row
        for i in range (2,m+1):
            for j in range(1,n+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]
        return dp[m][n]

