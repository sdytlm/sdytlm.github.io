class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 长度位i的数字中不同digit的数量
        nums = [9] 
        for x in range(9,0,-1):
            nums.append(nums[-1] * x)
        # nums[3]不包括nums[2]
        return sum(nums[:n])+1

