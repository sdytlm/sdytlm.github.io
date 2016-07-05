class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        #dp[i][j]: 某一行第i列 = List[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])
        #记住上一行的所有列的dp即可
        n = len(triangle)
        dp = [0]*n

        #init: from bottom to top
        for i in range(n):
            dp[i] = triangle[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = triangle[i][j]+min(dp[j],dp[j+1])
        return dp[0]
