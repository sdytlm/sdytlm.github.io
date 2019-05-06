class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        ret = 0
        min_end = -sys.maxint - 1
        for i in sorted(intervals, key=lambda i:i.end):
            # no overlap
            if i.start >= min_end:
                min_end = i.end
            else:
                ret += 1
        return ret
        
