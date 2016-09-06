class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        if N < 2:
            return 0

        A = min(nums)
        B = max(nums)

        # 一个bucket的数值范围
        bucketRange = max(1, int((B-A-1)/(N-1)) + 1)
        # bucket数组的长度
        bucketLen = (B-A) / bucketRange + 1
        # bucket数组
        buckets = [None]* bucketLen

        # 把nums中的数都放到bucket中
        for K in nums:
            # 找到K在哪个bucket里
            loc = (K-A)/bucketRange
            bucket = buckets[loc]

            if bucket is None:
                # 每一个bucket只维护在这个bucket中的数的最大和最小值
                bucket = {'min' : K, 'max' : K}
                buckets[loc] = bucket
            else:
                bucket['min'] = min(bucket['min'], K)
                bucket['max'] = max(bucket['max'], K)
           
        maxGap = 0
        for x in range(bucketLen):
            if buckets[x] != None:
                # next bucket的位置
                y = x+1
                # 找到一个飞空的bucket
                while y < bucketLen and buckets[y] == None:
                    y += 1
                if y < bucketLen:
                    maxGap = max(maxGap, buckets[y]['min'] - buckets[x]['max'])
                x = y
        return maxGap
