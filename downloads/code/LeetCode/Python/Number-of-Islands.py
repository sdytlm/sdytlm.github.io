class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        ret = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] != '1':
                    continue
                ret += 1
                self.dfs(i,j,grid)
        return ret
    def dfs(self,i,j,grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '2'
        self.dfs(i-1,j,grid)
        self.dfs(i+1,j,grid)
        self.dfs(i,j-1,grid)
        self.dfs(i,j+1,grid)

