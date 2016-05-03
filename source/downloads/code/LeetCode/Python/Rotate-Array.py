class Solution(object):
    def revert(self,nums,start,end):
        i = start
        j = end
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k<0:
            return 

        # reverse the whole array
        self.revert(nums,0,len(nums)-1)
        # reverse left k
        self.revert(nums,0,k-1)

        # reverse right n-k
        self.revert(nums,k,len(nums)-1)           
