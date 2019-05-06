class Solution(object):
    def power(self, x, n):
        if n == 0:
            return 1
        v = self.power(x,n/2)
        if n%2 == 0:
            return v*v
        else:
            return v*v*x

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # Divide and Merge
        # nlog(n)

        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            return 1/self.power(x,-n)
        else:
            return self.power(x,n)
