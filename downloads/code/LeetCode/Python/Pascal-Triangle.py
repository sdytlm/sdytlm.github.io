class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows < 1:
            return ret
        ret.append([1])
        if numRows == 1:
            return ret

        for i in range(1,numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(ret[i-1][j] + ret[i-1][j-1])
            tmp.append(1)
            ret.append(tmp[:])
        return ret
