class Solution(object):
    def subset_helper(self, nums, result, vector):
        result.append(vector[:])

        for i in range(len(nums)):
            # duplicated
            if i>0 and nums[i] == nums[i-1]:
                continue

            vector.append(nums[i])
            self.subset_helper(nums[i+1:],result,vector)
            vector.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums == None:
            return result
        self.subset_helper(sorted(nums), result,[])
        return result
