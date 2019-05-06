class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        if not wordDict:
            return len(s)==0

        n = len(s)
        dp = [False]*(n+1)

        dp[0] = True

        for i in range(1,n+1):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[n]


