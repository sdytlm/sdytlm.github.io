class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # this two tables are really important
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = ""
        for i in range(len(nums)):
            # it is not "if", because nums[i] could appear twice
            while num >= nums[i]:
                result += romans[i]
                num -= nums[i]

        return result
