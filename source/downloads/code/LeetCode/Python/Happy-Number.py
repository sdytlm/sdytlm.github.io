class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return False
        hash_table = dict()
        while True:
            if n == 1:
                return True
            hash_table[n] = 1
            
            n = sum([int(x)*int(x) for x in list(str(n))]) 
            if n in hash_table:
                return False

