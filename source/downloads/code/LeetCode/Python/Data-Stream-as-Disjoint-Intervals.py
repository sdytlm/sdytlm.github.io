# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = [] 

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        def upper_bound(nums, target):
            # 基于nums[i].start, 二分查找
            left, right = 0, len(nums)-1
            while left<=right:
                mid = (left+right)/2
                if nums[mid].start > target:
                    right = mid-1
                else:
                    left = mid+1
            return left
        i = upper_bound(self.intervals, val)

        # 插入target以后，合并各个intervals
        # 新集合的start，end
        start, end = val, val
        # target 和 intervals[i]有交集
        if i !=0 and self.intervals[i-1].end+1 >= val:
            i -= 1

        while i != len(self.intervals) and end+1 >= self.intervals[i].start:
            # 有交集
            start = min(start,self.intervals[i].start)
            end = max(end,self.intervals[i].end)
            del self.intervals[i]
        # 插入新的区间
        self.intervals.insert(i,Interval(start,end))
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


#Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
