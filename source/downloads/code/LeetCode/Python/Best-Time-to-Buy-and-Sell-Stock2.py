class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        # 递增序列起点
        buy = 0
        # 递增序列终点
        sell = 0
        ret = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[sell]:
                ret += prices[sell]-prices[buy]
                buy = i
                sell = i
            else:
                sell = i

        # 1,2,3,4
        if sell>buy:
            ret += prices[sell]-prices[buy]

        return ret
