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

        if target<matrix[0][0] or target>matrix[row-1][col-1]:
            return False

        l = 0
        r = row*col-1

        while l<=r:
            m = (l+r)/2
            if matrix[m/col][m%col] == target:
                return True
            elif matrix[m/col][m%col] < target:
                l = m+1
            else:
                r = m-1
        return False
