class Solution(object):
    def search(self, nums, left, right):
        if nums[left] <= nums[right]:
            return nums[left]
        mid = (left+right)/2
        return min(self.search(nums,left,mid), self.search(nums,mid+1,right))
    
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums,0,len(nums)-1)
