class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)

        # 若总共有偶数，找到第(l1+l2)/2 和 (l1+l2)/2+1的平均数
        if (l1+l2)%2 == 0:
            return (self.findKth(nums1,nums2,(l1+l2)/2) + self.findKth(nums1,nums2,(l1+l2)/2+1))/2.0
        else:
        # 若总共有奇数，找到第(l1+l2)/2+1个就是答案
            return self.findKth(nums1,nums2,(l1+l2)/2+1)

    def findKth(self, nums1, nums2, k):
        # 确保nums1个数比nums2少
        if len(nums1) > len(nums2):
            return self.findKth(nums2,nums1,k)
        
        # 第k个就是nums[k-1]
        if len(nums1) == 0:
            return nums2[k-1]
        # 若程序到这里，说明至少每个数组都有1个元素
        if k == 1:
            return min(nums1[0],nums2[0])

        pa = min(k/2, len(nums1))
        pb = k-pa

        if nums1[pa-1] <= nums2[pb-1]:
            #第k个一定在nums2中
            return self.findKth(nums1[pa:], nums2, k-pa)
        else:
            # 第k个一定在nums1中
            return self.findKth(nums1,nums2[pb:], k-pb)

if __name__ == "__main__":
    sol = Solution()
    sol.findMedianSortedArrays([1,2],[3,4])
