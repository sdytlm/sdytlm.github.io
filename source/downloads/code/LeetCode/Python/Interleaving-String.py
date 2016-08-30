class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 is None or s2 is None or s3 is None:
            return False

        # dp[i][j]: s1[:i-1], s2[:j-1] 是否能交替组成s3[:i+j+1]
        l1 = len(s1)
        l2 = len(s2)
        if l1+l2 != len(s3):
            return False

        dp = [[False for i in range(l2+1)] for j in range(l1+1)]
        
        dp[0][0] = True
        
        # 不要s2，只有s1 合成s3
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        # 不要s1, 只有s2 合成s3
        for i in range(1, l2+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]

        for i in range(1,l1+1):
            for j in range(1,l2+1):
                # 因为s1[i-1] == s3[i+j-1], 去比较dp[i-1][j]
                # 因为s2[j-1] == s3[i+j-11], 去比较dp[i][j-1]
                dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        return dp[l1][l2]
