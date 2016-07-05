class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack:
            return 0
        if needle == "":
            return 0
        i = 0
        while i < len(haystack)-len(needle)+1:
            j = 0
            tmp = i
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i+=1
                j+=1
            if j == len(needle):
                return tmp
            i = tmp+1
        return -1
