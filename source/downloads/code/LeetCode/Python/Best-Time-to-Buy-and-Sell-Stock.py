class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        n = len(prices)
        
        # 每一天卖出能赚到的最大钱
        dp = [0]*n
        # 当前为止股价最低值
        cur_min = prices[0]
        
        for p in range(len(prices)):
            if prices[p] <= cur_min:
                dp[p] = 0
                cur_min = prices[p]
            else:
                dp[p] = prices[p] - cur_min
        return max(dp)
        
