class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        col = dict()
        for i in range(26):
            col[str(unichr(65+i))] = i+1
        ret = 0
        for i in range(len(s)-1,-1,-1):
            ret += col[s[i]]*(26 ** (len(s)-i-1))
        return ret


