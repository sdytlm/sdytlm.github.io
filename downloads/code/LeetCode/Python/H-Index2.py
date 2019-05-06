class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start = 0
        end = len(citations)-1

        while start <= end:
            mid = (start + end)/2
            if citations[mid] < len(citations)-mid:
                start = mid+1
            else:
                end = mid-1
        return len(citations)-start
