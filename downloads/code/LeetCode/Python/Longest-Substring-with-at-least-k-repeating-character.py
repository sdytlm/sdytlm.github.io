class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        for x in set(s):
            # x没有重复k次
            if s.count(x) < k:
                return max(self.longestSubstring(t,k) for t in s.split(x))
        # 所有s中字符都符合
        return len(s)
