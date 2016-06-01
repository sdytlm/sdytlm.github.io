class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        size = len(nums)
        result = size+1
        sum = 0
        while end<size:
            # find the end
            while end<size and sum < s:
                sum += nums[end]
                end += 1
            # find the start
            while start<end and sum >= s:
                result = min(result,end-start)
                sum -= nums[start]
                start += 1
        if result <= size:
            return result
        else:
            return 0
