class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        l = 0
        r = len(s)-1
        alpha = "0123456789abcdefghijklmnopqrstuvwxyz"
        while l<r:
            while l < r and s[l] not in alpha:
                l += 1
            if l >= r:
                return True

            while l<r and s[r] not in alpha:
                r -= 1

            if l == r:
                return True

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
