class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            if matrix[i][0] <= target and matrix[i][col-1] >=target:
                if self.searchRow(matrix,i,target) == True:
                    return True
        return False

    def searchRow(self, matrix, row, target):
        n = len(matrix[0])
        l = 0
        r = n-1
        # Binary search
        while l <= r:
            m = (l+r)/2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m-1
            else:
                l = m+1
        return False

if __name__ == "__main__":
    sol = Solution()
    print sol.searchMatrix([[-1,3]],-1)
