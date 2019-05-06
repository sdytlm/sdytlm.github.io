class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        hash_map = dict()
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                return True
        return False
