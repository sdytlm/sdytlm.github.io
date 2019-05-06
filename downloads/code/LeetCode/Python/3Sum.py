class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret = []
        if not nums:
            return ret

        nums = sorted(nums)

        n = len(nums)
        for i in range(n):
            l = i+1
            r = n-1
            while l<r:
                val = nums[i]+nums[l]+nums[r]
                if val == 0:
                    ret.append(sorted([nums[l],nums[i],nums[r]]))
                    # should not break "-2,0,1,1,2"
                    l += 1
                elif val < 0:
                    l += 1
                else:
                    r -= 1
        return [list(t) for t in set(tuple(element) for element in ret)]
