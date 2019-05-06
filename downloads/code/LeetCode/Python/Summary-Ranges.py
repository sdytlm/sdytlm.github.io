class Solution(object):
    def findNext(self, nums, index):
    # if index is the last one
        if index == len(nums)-1:
            return index

        while index < len(nums)-1 and nums[index] == nums[index+1]-1:
            index += 1
        return index

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if nums == None or len(nums) == 0:
            return result
        l = len(nums)
        index = 0
        while index < l:
            end = self.findNext(nums,index)
            # single
            if end == index:
                result.append(str(nums[index]))
            else:
                # range
                s = str(nums[index])+"->"+str(nums[end])
                result.append(s)
            index = end+1
        return result
