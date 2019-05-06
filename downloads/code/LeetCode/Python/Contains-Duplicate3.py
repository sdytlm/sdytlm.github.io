class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        if k < 1 or t < 0:
            return False
        Dict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x]/max(1,t)
            # only check three options
            for m in (key-1,key,key+1):
                if m in Dict and abs(Dict[m]-nums[x])<=t:
                    return True
            Dict[m] = nums[x]
            if x >= k:
                Dict.popitem(last=False)
        return False
