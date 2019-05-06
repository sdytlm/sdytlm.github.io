class Solution(object):
    def recur_combine(self, result, vector, i, n, k):
        if len(vector) == k:
            result.append(vector[:])
            return
        
        while i <= n:
            vector.append(i)
            self.recur_combine(result,vector,i+1,n,k)
            vector.pop()
            i = i+1
        return 


    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        result = []
        if n < k:
            return result
        self.recur_combine(result, [], 1, n, k)
        return result
