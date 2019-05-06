class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0]*(col) for i in range(row)]

        dp[0][0] = 1
        for i in range(1,row):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
        for j in range(1,col):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0

        for i in range(1,row):
            for j in range(1,col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[row-1][col-1]
        
