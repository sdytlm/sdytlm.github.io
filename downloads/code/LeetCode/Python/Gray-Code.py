class Solution(object):                                                                  
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        # start from n == 0
        seq = self.grayCode(n-1)
        result = seq
        for i in reversed(seq):
            result.append(i | (1<<(n-1)))
        return result
