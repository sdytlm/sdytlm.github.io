class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == None and word2 == None:
            return 0
        elif word1 == None:
            return len(word2)
        elif word2 == None:
            return len(word1)

        l1 = len(word1)
        l2 = len(word2)
        
        dp = [[0]*(l1+1) for x in range(l2+1)]
        # 初始化dp
        for i in range(l2+1):
            dp[i][0] = i
        for i in range(l1+1):
            dp[0][i] = i
        
        for i in range(1,l2+1):
            for j in range(1,l1+1):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
        return dp[l2][l1]
