class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #
        if len(prices) <2:
            return 0

        n = len(prices)
        buy = [0] * n
        sell = [0] * n

        # 第0天买入，第1天卖掉 或者 不卖
        sell[1] = max(0,prices[1]-prices[0])
        
        # 并没有卖出的时候，买入相当于-prices[i]
        buy[0] = -prices[0]
        # 要么是第一天买，要么是第二天买
        buy[1] = max(-prices[1], -prices[0])

        for i in range(2,n):
            buy[i] = max(buy[i-1], sell[i-2]-prices[i])
            sell[i] = max(sell[i-1], prices[i]+buy[i-1])

        return sell[n-1]
