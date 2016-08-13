class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = dict()
        for i in range(len(nums)):
            idx = hash_map.get(nums[i])
            if idx >= 0 and k>= i-idx:
                    return True
            hash_map[nums[i]] = i
        return False
