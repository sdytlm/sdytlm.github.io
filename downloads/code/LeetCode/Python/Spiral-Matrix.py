class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left = 0
        right = len(matrix[0])-1
        top = 0
        down = len(matrix)-1

        direct = 0 # 0: go right, 1: go down, 2:go left, 3:go up
        ret = []
        while True:
            if direct == 0:
                for i in range(left,right+1):
                    ret.append(matrix[top][i])
                top += 1
            if direct == 1:
                for i in range(top,down+1):
                    ret.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right,left-1,-1):
                    ret.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down,top-1,-1):
                    ret.append(matrix[i][left])
                left += 1
            if left > right or top > down:
                return ret

            direct = (direct+1)%4
