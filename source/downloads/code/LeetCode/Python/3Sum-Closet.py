class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = 0
        diff = sys.maxint
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                if abs(sum-target) < diff:
                    ret = sum
                    diff = abs(sum-target)
                if sum == target:
                    return ret
                elif sum>target:
                    k = k-1
                else:
                    j = j+1
        return ret
