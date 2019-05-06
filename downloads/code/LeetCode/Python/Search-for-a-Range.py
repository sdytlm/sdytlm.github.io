class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        ret = [-1,-1]
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end)/2
            if target == nums[mid]:
                break
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
        # Not found
        if start > end:
            return ret

        l = mid
        r = mid
	# Find range       
	while l>0 and  nums[mid] == nums[l-1]:
            l -= 1
        while r < end and nums[mid] == nums[r+1]:
            r += 1
        return [l,r]

