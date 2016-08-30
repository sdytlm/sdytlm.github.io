class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        hash_table = dict()
        for c in s:
            if hash_table.get(c) == None:
                hash_table[c] = 1
            else:
                hash_table[c] += 1

        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return i
        return -1
