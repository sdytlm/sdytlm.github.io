class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max = 2147483647
        if divisor == 0:
            return max
        neg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        a = abs(dividend)
        b = abs(divisor)

        ret = 0
        shift = 31

        while shift >= 0:
            if a >= (b<<shift):
                a -= b<<shift
                ret += 1<<shift
            shift -= 1

        if neg:
            ret = -ret
        if ret >= max:
            return max
        return ret
