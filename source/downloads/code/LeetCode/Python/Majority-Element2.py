class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums

        ret = []
        # two candidates
        n1 = 0
        n2 = 0
        # appear times for them
        c1 = 0
        c2 = 0

        for i in nums:
            # order is important
            if n1 == i:
                c1+=1
            elif n2 == i:
                c2+=1
            elif c1 == 0:
                c1 = 1
                n1 = i
            elif c2 == 0:
                c2 = 1
                n2 =i
            else:
                c1 -= 1
                c2 -= 1
        # count the appear time of two candidates
        if c1 != 0 and nums.count(n1) > len(nums)/3:
            ret.append(n1)
        if c2 != 0 and nums.count(n2)> len(nums)/3:
            ret.append(n2)
        return ret
