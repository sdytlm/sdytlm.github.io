 class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp[i] = dp[i-1]+dp[i-2]
        # i: length of s
        if not s:
            return 0
        # "01" -> 0
        if s[0] == '0':
            return 0

        # any s has "00" will not get result:
        if "00" in s:
            return 0

        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,len(s)+1):
            # [10,26] except 10 and 20
            if 10<=int(s[i-2:i])<=26 and s[i-1] !='0':
                dp[i] = dp[i-1]+dp[i-2]
            # 10,20
            elif s[i-2:i] == '10' or s[i-2:i] == '20':
                dp[i] = dp[i-2]
            # 1-9
            elif s[i-1] != '0':
                dp[i] = dp[i-1]
            else:
                return 0
        return dp[len(s)]
