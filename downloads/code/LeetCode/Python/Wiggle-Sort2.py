class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # O(nlog(n)) + O(n)
        sorted_list = sorted(nums)
        n = len(sorted_list)
        # fill odd position
        # sorted_list.pop will return the current larggest one
        for i in range(1,n,2):
            nums[i] = sorted_list.pop()
        # fill even position
        for i in range(0,n,2):
            nums[i] = sorted_list.pop()
