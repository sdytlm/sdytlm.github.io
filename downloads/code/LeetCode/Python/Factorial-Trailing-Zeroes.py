class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        ret = 0
        while n >= x:
            ret += n/x
            x *= 5
        return ret
        
