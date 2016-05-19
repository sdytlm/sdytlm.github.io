class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n^2: 
        # dp[i]: the longest increasing subsequence
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
        rt = 0
        for i in range(len(nums)):
            if rt < dp[i]:
                rt = dp[i]
        return rt

        # n(logn)
        # dp: is an array to record the longest increasing subsequence
        dp = []
        for i in range(len(nums)):
            start = 0
            end = len(dp)-1
            # binary search dp, find the place dp[mid] < nums[i]
            while start <= end:
                mid = (start+end)/2
                if dp[mid] >= nums[i]:
                    end = mid - 1
                else:
                    start = mid + 1
            if start >= len(dp):
                dp.append(nums[i])
            else:
                dp[start] = nums[i]
        return len(dp)
