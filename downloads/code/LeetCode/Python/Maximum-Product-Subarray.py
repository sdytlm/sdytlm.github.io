 class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pos = []  # positive result array
        neg = []  # negative result array

        pos.append(nums[0])
        neg.append(nums[0])
        for i in range(1,len(nums)):
            pos.append(max(pos[i-1]*nums[i], neg[i-1]*nums[i], nums[i]))
            neg.append(min(pos[i-1]*nums[i], neg[i-1]*nums[i], nums[i]))
        # find the largest in pos array
        ret = pos[0]
        for i in pos:
            if ret < i:
                ret = i
        return ret      
