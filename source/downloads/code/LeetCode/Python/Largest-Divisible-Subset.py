class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # s[d] = set() # 最大数为ｄ的子集
        s = {1:set()}
        for x in sorted(nums):
            s[x] = max((s[d] for d in S if x%d == 0), key=len) | {x}
        return list(max(s.values(),key=len))


# DP
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        ret = []
        nums = sorted(nums)
        n = len(nums)
        # 最大值为nums[i]且满足条件的set，能有多少数dp[i]
        dp = [1]*n
        # 在一个解中，数x之前的数为prev[x]
        prev = [None]*n
        
        for x in range(n):
            for y in range(x):
                if nums[x] % nums[y] == 0 and dp[y]+1 > dp[x]:
                    dp[x] = dp[y]+1
                    prev[x] = y
        
        # nums[idx]有最大subset
        idx = dp.index(max(dp))
        ret = []

        while idx != None:
            ret.append(nums[idx])
            idx = prev[idx]
        return ret
