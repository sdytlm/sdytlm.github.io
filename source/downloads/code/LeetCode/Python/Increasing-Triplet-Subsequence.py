class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for the smallest value
        
        a = b = None
        for i in nums:
            if a == None or a >= i:
                a = i
            elif b == None or b >= i:
                b = i
            else:
                return True
        return False

