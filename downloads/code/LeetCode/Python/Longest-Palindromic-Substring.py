class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        bool dp = [[False]*1000 for x in range(1000)]
        n = len(s)
        maxLen = 1
        maxStart = 0
        
        # dp[i][i] = True
        for i in range(n):
            dp[i][i] = True
        
        # dp[i][i+1] = True if s[i] == s[i+1]
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                maxLen = 2
                maxStart = i

        # dp[i][j] = True if s[i]==s[j] and dp[i+1][j-1] == True
        for length in range(3,n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    maxLen = length
                    maxStart = i
        return s[maxStart,maxStart+maxLen]
