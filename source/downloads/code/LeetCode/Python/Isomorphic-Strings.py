class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sourceMap = dict()
        targetMap = dict()

        for i in range(len(s)):
            source = sourceMap.get(s[i])
            target = targetMap.get(t[i])
            if source == None and target == None:
                sourceMap[s[i]] = t[i]
                targetMap[t[i]] = s[i]
            elif source != t[i] or target != s[i]:
                return False
        return True

