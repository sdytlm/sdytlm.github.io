class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while(nums[i] != i+1):
                # 第三个条件是nums[i]要去的位置和现在的值相同，
                if nums[i] < 0 or nums[i] >= n or nums[i] == nums[nums[i]-1]:
                    break
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        # 所有的元素都在
        return n+1

        
