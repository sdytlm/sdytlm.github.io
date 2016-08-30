# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """


        ret = []
        if len(intervals) == 0:
            return ret

        intervals = sorted(intervals, key = lambda x: x.start)
        s = intervals[0].start
        e = intervals[0].end

        for interval in intervals:
            # 第一个interval 或者 没有重叠
            if len(ret) == 0 or ret[-1].end < interval.start:
                ret.append(interval)
            else:
                ret[-1].end = max(ret[-1].end, interval.end)
        return ret

