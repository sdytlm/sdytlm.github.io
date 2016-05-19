class Solution(object):
    def count(self,s):
        num = 1
        ret = ""
        for i,j in enumerate(s):
            if i+1 < len(s) and s[i] == s[i+1]:
                num += 1
            elif i+1 < len(s):
                ret = ret + str(num) + s[i]
                num = 1
        # last element
        ret = ret + str(num) + s[i]
        return ret
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = "1"
        for i in range(1,n):
            ret = self.count(ret)
        return ret
if __name__ == "__main__":
    sol = Solution()
    sol.countAndSay(2)
