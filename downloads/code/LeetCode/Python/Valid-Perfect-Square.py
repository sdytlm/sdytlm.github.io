class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return True

        r = num/2+1
        l = 2

        while l <= r:
            mid = (l+r)/2
            target = num/mid
            
            # num = 5
            if num%mid != 0 and target == mid:
                    return False
            
            if target == mid:
                return True
            
            if target < mid:
                r = mid-1
            else:
                l = mid+1
        return False



