class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        if not s:
            return ret

        words = s.split()
        for i in range(len(words)-1,-1,-1):
            ret = ret+words[i] + " "
        return ret[:len(ret)-1]
