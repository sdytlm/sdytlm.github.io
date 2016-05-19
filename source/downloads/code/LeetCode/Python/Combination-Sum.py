class Solution(object):
    def recur_helper(self,c,target,result,vector,cur):
        if target == 0:
            result.append(vector[:])
            return
        
        while cur<len(c):
            if c[cur] <= target:
                vector.append(c[cur])
                self.recur_helper(c,target-c[cur],result,vector,cur)
                vector.pop()
            cur += 1
        return

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []
        candidates = sorted(candidates)
        if candidates == None or len(candidates) == 0:
            return result
        self.recur_helper(candidates,target,result,[],0)
        return result
