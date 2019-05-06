class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i]: the least step needed to reach i dollars
        # dp[i+coin[j]] = min(dp[i]+1,dp[i+coin[j]])
        # dp[0] = 0
        dp = [0]+[0x7ffffffe] * (amount)
        
        for i in range(amount+1):
            for j in coins:
                if i +j <=amount:
                    dp[i+j] = min(dp[i]+1,dp[i+j])
        
         return dp[amount] if dp[amount] != 0x7ffffffe else -1      
