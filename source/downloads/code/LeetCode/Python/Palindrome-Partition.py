class Solution(object):
    def isParlindrome(self,s):
        start = 0
        end = len(s) - 1
        while start<end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    # DFS
    def partition_dfs(self, result, vector, s, start,end):
        if start >= end:
            result.append(vector)
            return

        for i in range(start,end):
            new_str = s[start:i+1]
            if self.isParlindrome(new_str):
                self.partition_dfs(result,vector+[new_str],s,i+1,end)
        return 
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if s == None:
            return result
        self.partition_dfs(result,[],s,0,len(s))
        return result
    
