class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        tmp = x
        num = 0
        # 确定位数
        while tmp/10 != 0:
            tmp =tmp/10
            num += 1
        # 个位数永远都是
        if num == 0:
            return True
        
        y = x
        # x从最高位，y从个位
        while y != 0 and x != 0:
            if x/(10**num) != y%10:
                return False
            x = x%(10**num)
            y = y/10
            num = num-1
        return True
