class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*n for x in range(m)]
        ret = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                ret = max(ret,dp[i][j])
        return ret*ret
        
