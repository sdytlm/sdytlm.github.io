class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        visited = [-1]*n
        self.ret = 0
        self.sol(visited, n, 0)
        return self.ret

    def sol(self, visited, n, index):

        def check(visited,row,col):
            for i in range(row):
                if visited[i] == col or abs(i-row) == abs(visited[i] - col):
                    return False
            return True

        if index == n:
            self.ret += 1
            return

        for j in range(n):
            if check(visited,index,j):
                visited[index] = j
                self.sol(visited,n,index+1)

