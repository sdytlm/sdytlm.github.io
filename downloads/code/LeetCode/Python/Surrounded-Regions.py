class Solution(object):
    def fill(self, board,queue,x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != 'O':
            return
        queue.append((x,y))
        board[x][y] = 'D'

    def bfs(self,board,queue,x,y):
        if board[x][y] == 'O':
            queue.append((x,y))
            self.fill(board,queue,x,y)

        # mark all neighbors
        while queue:
            cur = queue.pop(0)
            i = cur[0]
            j = cur[1]
            self.fill(board,queue,i-1,j)
            self.fill(board,queue,i,j-1)
            self.fill(board,queue,i,j+1)
            self.fill(board,queue,i+1,j)


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if board == None or len(board) == 0:
            return

        row = len(board)
        col = len(board[0])
        queue = []

        for i in range(row):
            self.bfs(board,queue,i,0)
            self.bfs(board,queue,i,col-1)

        for i in range(col):
            self.bfs(board,queue,0,i)
            self.bfs(board,queue,row-1,i)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'
        return
