class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0
        strs = s.split()
        # " "
        if len(strs) == 0:
            return 0
        return len(strs[-1])
