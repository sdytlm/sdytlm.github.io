class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = ['0','1','2','3','4','5','6','7','8','9']
        index = 0
        l = len(str)
        neg = 1

        # find the first non-space char
        while index < l and str[index] == ' ':
            index += 1
        if index == l:
            return 0

        # "+" or "-"
        if str[index] == '-':
            neg = -1
            index += 1

        if str[index] == '+':
            index += 1

        # get integer part
        integer = 0
        decimal = 1
        while index < l and str[index] in nums:
            integer = 10*integer + int(str[index])
            index += 1
        # maybe the decimal part
        if str[index] == '.':
            while index<l and str[index] in nums:
                integer = integer + int(str[index])/(10**decimal)
                index += 1
                decimal += 1
        
        integer = neg * integer
        if integer > sys.maxint:
            return sys.maxint
        elif integer < -sys.maxint:
            return -sys.maxint
        else:
            return integer

