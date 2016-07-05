class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hash_map = dict()
        for i in nums:
            if i in hash_map.keys():
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        # sort dict by hash_map.value
        sorted_map = sorted(hash_map.items(), key=operator.itemgetter(1),reverse=True)

        ret = []
        for i,j in sorted_map:
            ret.append(i)
            k -= 1
            if k == 0:
                return ret
        return ret
