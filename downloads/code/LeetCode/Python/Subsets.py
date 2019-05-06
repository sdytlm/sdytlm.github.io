class Solution(object):
    def find_sets(self,nums,ret,tmp,index,n):
        if len(tmp) == n:
            ret.append(tmp[:])
            return
        for i in range(index,len(nums)):
            tmp.append(nums[i])
            self.find_sets(nums,ret,tmp,i+1,n)
            tmp.pop()
        return 

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if not nums:
            return ret
        ret.append([])
        nums = sorted(nums)
        for i in range(1,len(nums)+1):
            self.find_sets(nums,ret,[],0,i)
        return ret
