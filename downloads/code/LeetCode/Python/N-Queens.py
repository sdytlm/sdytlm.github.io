class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []
        # 记录每一行当前Q在哪里
        visited = [-1]*n
        ret = []
        self.rec([],ret,visited,n,0)
        return ret



    def rec(self,board,ret,visited,n,index):
        
        def check(visited,row,col):
            for i in range(row):
                if visited[i] == col or abs(i-row) == abs(col-visited[i]):
                    return False
            return True


        if index == n:
            ret.append(board[:])
            return

        for j in range(n):
            # 第[index][j]可以被放queen
            if check(visited,index,j):
                visited[index] = j
                
                newstr = "."*n
                self.rec(board+[newstr[:j]+'Q'+newstr[j+1:]],ret,visited,n,index+1)
 
