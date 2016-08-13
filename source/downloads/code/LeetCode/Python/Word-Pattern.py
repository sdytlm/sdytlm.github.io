class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern:
            return False
        hash_table = dict()
        s_list = str.split(" ")
        if len(pattern) != len(s_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hash_table:
                # "abba" -> "dog dog dog dog"
                if s_list[i] in hash_table.values():
                    return False
                hash_table[pattern[i]] = s_list[i]
            else:
                if hash_table[pattern[i]] != s_list[i]:
                    return False
        return True
