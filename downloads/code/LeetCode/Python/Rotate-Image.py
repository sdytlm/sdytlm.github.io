class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ret = []
        if matrix == None:
            return ret

        n = len(matrix)
        for i in range(n):
            for j in range(n-i-1):
                matrix[i][j],matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1],matrix[i][j]
        matrix.reverse()
