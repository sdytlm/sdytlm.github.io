class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(numbers)-1
        while l < r:
            num = numbers[l] + numbers[r]
            if num == target:
                return [l+1,r+1]
            elif num < target:
                l = l+1
            else:
                r = r-1

