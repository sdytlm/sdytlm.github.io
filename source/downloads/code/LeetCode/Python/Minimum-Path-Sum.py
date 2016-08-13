class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp[i][j]: min path until grid[i][j]

        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        ret = [[0]*(col) for i in range(row)]
        
        for i in range(0,row):
            for j in range(0, col):
                if i == 0 and j == 0:
                    ret[i][j] = grid[i][j]
                elif i == 0:
                    ret[i][j] = ret[i][j-1] + grid[i][j]
                elif j == 0:
                    ret[i][j] = ret[i-1][j] + grid[i][j]
                else:
                    ret[i][j] = min(ret[i-1][j],ret[i][j-1]) + grid[i][j]
        return ret[row-1][col-1]

