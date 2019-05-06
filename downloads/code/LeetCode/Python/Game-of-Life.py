class Solution(object):
    def countLiveNeighbors(self, i,j,board,m,n):
        dx = [-1,-1,-1,0,0,1,1,1]
        dy = [-1,0,1,-1,1,-1,0,1]
        
        cnt = 0
        # 8 个邻居
        for k in range(8):
            nx = dx[k]+i
            ny = dy[k]+j
            if nx < 0 or ny < 0 or nx >=m or ny >= n:
                continue
            if board[nx][ny] == 1 or board[nx][ny] == 2:
                cnt += 1
        return cnt
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        

        m = len(board)
        n = len(board[0])

        if m == 0 or n == 0:
            return

        for i in range(m):
            for j in range(n):
                cnt = self.countLiveNeighbors(i,j,board,m,n)
                # board[i][j] != 0
                if board[i][j]:
                    if cnt != 2 and cnt != 3:
                        board[i][j] = 2
                else:
                # board[i][j] == 0
                    if cnt == 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                board[i][j] &= 1

