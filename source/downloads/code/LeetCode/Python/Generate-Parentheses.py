class Solution(object):
    def getParenthesis(self, l, r, tmp, ret):
        # 有括号比左括号多
        if r < l:
            return
        if l ==0 and r == 0:
            ret.append(tmp)
        
        if l > 0:
            self.getParenthesis(l-1,r,tmp+'(',ret)
        if r > 0:
            self.getParenthesis(l,r-1,tmp+')',ret)


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ret = []
        if n == 0:
            return ret

        self.getParenthesis(n,n,"",ret)
        return ret
