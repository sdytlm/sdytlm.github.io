import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = random.choice(nums)
        # 放比pivot大的num
        nums1 = []
        # 放比pivot小的num
        nums2 = []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            if num < pivot:
                nums2.append(num)
        # 答案在num1中
        if k <= len(nums1):
            return self.findKthLargest(nums1,k)
        # 答案在num2中，不等式右边表示和pivot相等的nums数加len(nums1)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2,k-(len(nums)-len(nums2)))
        # 若k<=len(nums)-len(nums2)说明,第k大不在num1中，他和pivort相等
        return pivot
