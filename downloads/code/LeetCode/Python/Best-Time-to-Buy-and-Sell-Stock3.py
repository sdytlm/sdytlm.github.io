class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # f1,f2
        length = len(prices)
        if length == 0:
            return 0

        f1 = [0]*length
        f2 = [0]*length

        minV = prices[0]

        for i in range(1,length):
            f1[i] = max(f1[i-1],prices[i]-minV)
            minV = min(minV, prices[i])

        maxV = prices[length-1]
        for i in range(length-2,-1,-1):
            f2[i] = max(f2[i+1],maxV-prices[i])
            maxV = max(maxV, prices[i])
        ret = 0
        for i in range(length):
            if f1[i]+f2[i] > ret:
                ret = f1[i]+f2[i]
        return ret
