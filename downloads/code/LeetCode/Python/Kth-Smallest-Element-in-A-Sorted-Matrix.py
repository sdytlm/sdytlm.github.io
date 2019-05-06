class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n-1][n-1]

        while l <= r:
            mid_val = (l+r)/2
            cnt = self.countLowerNumbers(matrix, mid_val)
            if cnt < k:
                l = mid_val+1
            else:
                r = mid_val-1
        return l

    def countLowerNumbers(self,matrix,mid_val):
        # 从左下角开始统计相等或者小于mid_val的数量
        n = len(matrix)
        i = n-1
        j = 0
        cnt = 0
        while i >=0 and j < n:
            if mid_val >= matrix[i][j]:
                # 整个一列都是小于mid_val
                cnt += i+1
                j += 1
            else:
                i -= 1
        return cnt
