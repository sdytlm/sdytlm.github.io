class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)-1
        addon = 1
        for i in range(n,-1,-1):
            newval = digits[i]+addon
            digits[i] = newval%10
            if newval < 10:
                return digits
            addon = newval / 10
        if addon == 1:
            digits.insert(0,1)
        return digits
        
