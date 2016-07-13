class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # "1" appear once
        t1 = 0
        # "1" appear twice
        t2 = 0
        # "1" appear three times
        t3 = 0

        for i in nums:
            # update t2
            t2 |= t1 & i
            # update t1
            t1 = t1 ^ i
            # check which bits appear three times
            t3 = (t1 & t2)

            # put those bits to 0
            t1 &= ~t3
            t2 &= ~t3
        return t1
