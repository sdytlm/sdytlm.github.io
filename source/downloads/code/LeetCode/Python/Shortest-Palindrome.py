class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        rev_s = s[::-1]
        # 构造一个字符串
        l = s + '#' + rev_s
        # 
        p = [0]*len(l)
        # 字符串匹配KMP
        for i in range(1, len(l)):
            j = p[i-1]
            while j > 0 and l[i] != l[j]:
                j = p[j-1]
            p[i] = j+(l[i] == l[j])
        return rev_s[: len(s)-p[-1]]+s
