class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1 # 从１开始枚举，题目要求
        r = len(nums)-1

        while l <= r:
            m = (l+r)/2
            
            # 计算不大于m的个数，m 不是位置，而是枚举的数字
            sums = sum(x<=m for x in nums)
            if sums > m:
                r = m-1
            else:
                l = m+1
        return l
