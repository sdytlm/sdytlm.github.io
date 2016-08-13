 class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums

        nums = sorted(nums)
        ret = []
        n = len(nums)
        for i in range(0,n-3):
            # skip all redundant element
            if i!=0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(n-1,i+2,-1):
                # skipp repeated elements
                if j != n-1 and nums[j] == nums[j+1]:
                    continue
                l = i+1
                r = j-1
                while l < r:
                    val = nums[i]+nums[j]+nums[l]+nums[r]
                    if val == target:
                        ret.append([nums[i],nums[l],nums[r],nums[j]])
                        l += 1
                        r -= 1
                        # skip repeated element
                        while l<r and nums[l] == nums[l-1]:
                            l += 1
                        while l<r and nums[r] == nums[r+1]:
                            r = r-1
                            
                    elif val < target:
                        l = l+1
                    else:
                        r = r-1
        return ret      
