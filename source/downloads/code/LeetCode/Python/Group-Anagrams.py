class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ret = []
        # hash_map: <strs[i], 和strs[i]互为anagrams的其他字符串>
        hash_map = dict()
        for i , s in enumerate(strs):
            target = "".join(sorted(s))
            if target not in hash_map:
                hash_map[target] = [s]
            else:
                hash_map[target].append(s)
        
        for l in hash_map.values():
            # l 就是所有anagrams的列表
            ret.append(sorted(l))
        
        return ret
