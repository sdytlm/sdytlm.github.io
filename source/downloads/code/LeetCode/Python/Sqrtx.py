class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x

        if x == 0 or x == 1:
            return x
        while l <= r:
            m = (l+r)/2
            if m*m == x:
                return m
            elif m*m < x:
                l = m+1
            else:
                r = m-1
        return l-1
