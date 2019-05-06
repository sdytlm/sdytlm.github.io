class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        ret = []
        if not s:
            return ret
        
        self.findIP(s,ret,"",0)
        return ret

    def findIP(self,s,ret,tmp,r):
        if r == 4:
            if not s:
                ret.append(tmp[:len(tmp)-1])
            return
        

        for i in range(1,4):
            # 这里是等号，否则当s只有一个字符的时候,就不执行下面代码了
            if i <= len(s):
                ip = s[:i]
                if int(ip) <= 255:
                    self.findIP(s[i:],ret,tmp+ip+".",r+1)
                # make sure "00" "01" will not happen
                if s[0] == "0":
                    break
        return
if __name__ == "__main__":
    sol = Solution()
    sol.restoreIpAddresses("0000")
