class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if number == 1:
            return True

        while num != 1:
            if num%5==0:
                num = num/5
            elif num%3 ==0:
                num = num/3
            elif num%2==0:
                num = num/2
            else:
                break

        if num == 1:
            return True
        else:
            return False
