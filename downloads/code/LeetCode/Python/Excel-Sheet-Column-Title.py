class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # ord('A') = 65
        ret = ""
        while n > 0:
            ret = unichr(65+(n-1)%26)+ret
            n = (n-1)/26
        return ret
