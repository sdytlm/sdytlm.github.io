# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
    
        if not intervals:
            return [newInterval]

        s_index = 0
        e_index = len(intervals)-1

        for i in range(len(intervals)):
            if self.find(intervals[i],newInterval.start):
                s_index = i
        
        for i in range(len(intervals)-1,-1,-1):
        if self.find(intervals[i],newInterval.end):
                e_index = i

        newInt = [intervals[s_index].start, intervals[e_index].end]
        for x in range(s_index,e_index+1):
            del intervals[x]
        intervals.insert(s_index,newInt)
        return intervals
    def find(self, intervals, val):
        if val <= intervals.end and val >= intervals.start:
            return True
