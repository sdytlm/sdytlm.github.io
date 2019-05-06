class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        # use triangle to store the min value
        # From bottom to top
        if triangle == None:
            return 0
        
        if len(triangle) == 1 and len(triangle[0]) == 1:
            return triangle[0][0]

        row = len(triangle)
        for i in range(row-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

if __name__ == "__main__":
    sol = Solution()
    print sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
