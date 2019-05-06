class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        p = 0
        while m!=n:
            m = m>>1
            n = n>>1
            p+=1
        return m<<p
