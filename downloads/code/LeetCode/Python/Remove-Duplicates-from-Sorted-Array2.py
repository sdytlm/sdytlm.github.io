class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == None or len(nums) == 0:
            return 0

        start = 0
        # first element nums[end] != nums[start]
        end = 0
        index = 0

        while start < len(nums):
            end = self.findRec(nums,start)
            nums[index] = nums[start]
            index += 1
            if end - start >= 2:
                nums[index] = nums[start]
                index += 1
            start = end
        return index


    def findRec(self, nums, start):
        while start + 1 < len(nums):
            if nums[start] != nums[start+1]:
                return start+1
            start += 1
        return start+1
