class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        if x < 0:
            isNeg = True
            x = -x
        ret = 0
        
        if x == 0:
            return ret

        while x != 0:
            ret = 10 * ret + (x%10)
            x = x/10
        
        if isNeg == True:
            ret = -ret
        if ret < -(1<<31) or ret > (1<<31)-1:
            return 0
        return ret
