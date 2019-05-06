class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        sum = 0
        for i in nums:
            # if sum > 0, then add i, no matter i>0 or i<0
            if sum > 0:
                sum += i
            else:
            # if sum < 0, then make sum start over from i
                sum = i
            if sum > maxSum:
                maxSum = sum
        return maxSum
        
        
