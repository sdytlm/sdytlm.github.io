class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 1
        if n == 1 or n == 2:
            return ret
        if n== 3:
            return 2
        while n >= 2:
            # try 3 first
            if n % 3 ==0:
                n = n-3
                ret *= 3
            # if n%3 !=0 try 2
            elif n%2 ==0:
                n = n-2
                ret *=2
            else:
            # for others, use 3. Like 5 
                n = n-3
                ret *=3
        return ret
