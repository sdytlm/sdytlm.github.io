class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        ret =0
        while n > 0:
            ret += (n+8)/10*a + (n%10 == 1) * b
            b += n%10 *a
            a *= 10
            n /= 10
        return ret
                                                    
