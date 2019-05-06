class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_map = dict()
        ret = []
        if len(nums1) == 0 or len(nums2) == 0:
            return ret
        for i in range(len(nums1)):
            hash_map[nums1[i]] = i
        for i in nums2:
            if i in hash_map:
                ret.append(i)
                # 以防重复元素添加到ret
                del hash_map[i]
        return ret      
