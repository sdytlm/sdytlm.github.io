class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [0]*len(nums)
        if not nums:
            return ret
        product = 1
        
        n = 0
        for i in nums:
            if i == 0:
                n += 1
            else:
                product *= i
        # if nums contains more than two "0", return 0
        if n>1:
            return ret

        for i in range(len(nums)):
            if nums[i] == 0:
                ret[i] = product
            else:
                # if nums have one "0"
                if n == 1:
                    ret[i] = 0
                else:
                    ret[i] = product/nums[i]
        return ret
