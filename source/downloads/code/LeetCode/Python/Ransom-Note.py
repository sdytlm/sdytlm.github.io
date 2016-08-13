class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_map = dict()
        for i in magazine:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        for i in ransomNote:
            if i not in hash_map:
                return False
            if hash_map[i] == 0:
                return False
            hash_map[i] -= 1
        return True
