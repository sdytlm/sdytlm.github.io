class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        # hq: heap_queue<sum,index1,index2>
        hq = []

        def push(index1,index2):
            if index1<len(nums1) and index2<len(nums2):
                heapq.heappush(hq, [nums1[index1]+nums2[index2], index1, index2])
        
        push(0,0)
        ret = []
        while hq and len(ret) < k:
            # 当前最小的组合
            sums,i,j=heapq.heappop(hq)
            ret.append([nums1[i],nums2[j]])
            
            # 把下一个nums1[i],nums2[j+1]放进去
            push(i,j+1)
            
            # 若j==0, 并不知道nums1[i],nums2[0]和nums1[i],nums2[j+1]的关系
            if j==0:
                push(i+1,0)
        return ret
