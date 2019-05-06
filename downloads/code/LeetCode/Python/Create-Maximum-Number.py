class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 在数组中找到长度为k的最大子数组
        def find_max_sub_array(nums, k):
            # 维护当前最大子数组
            stack = []
            n = len(nums)
            for i in range(n):
                # 若stack已满，而且nums[i]比stack最后一个要大,则把stack[-1]弹出，插入nums[i]
                while stack and len(stack) + n - i > k and nums[i] > stack[-1]:
                    stack.pop()
                if len(stack) < k:
                    stack.append(nums[i])
            return stack


        l1 = len(nums1)
        l2 = len(nums2)

        ret = [0]*k
        for i in range(max(0,k-l2), min(k,l1)+1):
            sub1 = find_max_sub_array(nums1, i)
            sub2 = find_max_sub_array(nums2, k-i)
            ret = max(ret, [max(sub1,sub2).pop(0) for x in range(k)])
        return ret
