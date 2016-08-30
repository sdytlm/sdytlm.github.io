class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # counts 存了nums1[i]出现的次数
        counts = collections.Counter(nums1)
        ret = []
        for i in nums2:
            if counts[i] > 0:
                ret.append(i)
                counts[i] -= 1
        return ret
        
