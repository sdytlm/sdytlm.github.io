class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        R2Imap = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        ret = 0
        if s == "":
            return ret

        index = len(s)-2
        while index >=0:
            # CM, IV, IX 
            if R2Imap[s[index]] < R2Imap[s[index+1]]:
                ret -= R2Imap[s[index]]
            else:
            # M,D,C,L,X,V,I
                ret += R2Imap[s[index]]
            index -= 1
        # s[len(s)-1]
        ret += R2Imap[s[-1]]
        return ret
