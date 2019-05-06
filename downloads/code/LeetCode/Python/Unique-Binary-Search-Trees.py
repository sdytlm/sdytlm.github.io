class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dp: how many unique trees
        #dp[1] = 1
        #dp[2] = 2
        #dp[3] = 5 = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]
        #dp[n] = sum(dp[i] * dp[n-i-1])

        dp = [1,1,2]
        if n < 3:
            return dp[n]

        for i in range(3,n+1):
            sum = 0
            for j in range(0,i):
                sum += dp[j]*dp[i-j-1]
            dp.append(sum)
        return dp[n]
