class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = [] # 数组的比较小的部分， 最小堆 (存储负数) small[0] 的正数其实是small中最大的
        self.large = [] # 数组的比较大的部分, 最小堆 (存储正数)

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small,-num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large,num))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0]-self.small[0])/2.0
        else:
            return float(self.large[0])
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian() 
