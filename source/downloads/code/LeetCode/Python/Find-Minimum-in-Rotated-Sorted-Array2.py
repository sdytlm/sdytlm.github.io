class Solution(object):
        def findMin(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            l = 0
            r = len(nums)-1

            # l,r 不相等，为了解决[1]的问题
            while l < r:
                m = (l+r)/2
                # m在最小值的左边
                if nums[m] > nums[r]:
                    l = m+1
                # m 在最小值的右边
                elif nums[m] < nums[r]:
                    # m 有可能是答案
                    r = m
                else:
                    return min(self.findMin(nums[:m+1]), self.findMin(nums[m+1:]))
            return nums[l]

