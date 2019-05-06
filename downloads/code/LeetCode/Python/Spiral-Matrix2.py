class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        ret = [[0]*n for i in range(n)]
        direct = 0 # 0: go right, 1: go down, 2: go left, 3: got up

        l = 0
        r = n-1
        u = 0
        d = n-1
        num = 1

        while l<=d and u <= d:
            if direct ==0:
                for i in range(l,r+1):
                    ret[u][i] = num
                    num += 1
                u += 1
                direct = 1
            elif direct == 1:
                for i in range(u,d+1):
                    ret[i][r] = num
                    num += 1
                r -= 1
                direct = 2
            elif direct == 2:
                for i in range(r,l-1,-1):
                    ret[d][i] = num
                    num += 1
                d -= 1
                direct = 3
            else: # direct == 3
                for i in range(d,u-1,-1):
                    ret[i][l] = num
                    num += 1
                l += 1
                direct = 0
        return ret

