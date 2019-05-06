class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return

        fr = False
        fc = False

        row = len(matrix)
        col = len(matrix[0])

        # check first col
        for i in range(row):
            if matrix[i][0] == 0:
                fc = True
                break

        # check first row
        for i in range(col):
            if matrix[0][i] == 0:
                fr = True
                break
        
        # use first row and col to store the status of other rows/cols
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # update row/col except first row/col
        for i in range(1,row):
            if matrix[i][0] == 0:
                for j in range(1,col):
                    matrix[i][j] = 0

        for i in range(1,col):
            if matrix[0][i] == 0:
                for j in range(1,row):
                    matrix[j][i] = 0

        # update the first row/col
        if fr:
            for i in range(0,col):
                matrix[0][i] = 0
        if fc:
            for i in range(0,row):
                matrix[i][0] = 0
        return
