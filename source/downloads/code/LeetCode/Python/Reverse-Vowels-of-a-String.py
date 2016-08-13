class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        l = 0
        r = len(s)-1
        ret = [i for i in s]
        vowel = "aeiouAEIOU"
        while l < r:
            # find the vowel from left
            while l < r and ret[l] not in vowel:
                l += 1

            # find the vowel from right
            while l < r and ret[r] not in vowel:
                r -= 1

            if l<r:
                ret[l],ret[r] = ret[r],ret[l]
            l += 1
            r -= 1
        return "".join(ret)
