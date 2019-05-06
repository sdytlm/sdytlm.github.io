class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        n = len(strs)
        if n == 0:
            return ret
        for cur in range(len(strs[0])): 
            c = strs[0][cur]
            for i in range(1,n):
                # cur可能超过strs[i]的长度
                if cur >= len(strs[i]) or strs[i][cur] != c:
                    return strs[0][:cur]
        return strs[0]
            
