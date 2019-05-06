class Solution(object):                                                                          
    def comb_rec(self, c, target, ret, tmp,index):
        if target == 0 and tmp not in ret:
            ret.append(tmp[:])
            return
        if target < 0:
            return

        for i in range(index,len(c)):
            if target-c[i] < 0:
                return
            tmp.append(c[i])
            self.comb_rec(c,target-c[i],ret,tmp,i+1)
            tmp.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        ret = []
        if not candidates:
            return ret
        self.comb_rec(candidates,target,ret,[],0)
        return ret
