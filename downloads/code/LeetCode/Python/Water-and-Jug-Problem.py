class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def findGCD(x,y):
            if x == 0:
                return y
            return findGCD(y%x,x)

        if x > y:
            x,y = y,x

        gcd = findGCD(x,y)
        if gcd == 0:
            return z == 0
        return z % gcd == 0 and z <= x+y
