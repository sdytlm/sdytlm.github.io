class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []

        self.findSol(k,n,ret,[],1)
        return ret

    def findSol(self,k,n,ret,tmp,val):
        if n < 0:
            return
        if k == 0:
            if n != 0:
                return
            else:
                ret.append(tmp[:])
                return
        for i in range(val,10):
            tmp.append(i)
            self.findSol(k-1,n-i,ret,tmp,i+1)
            tmp.pop()
        return
