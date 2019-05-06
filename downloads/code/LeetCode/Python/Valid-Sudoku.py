class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def check(x,y,board):
            # 检查横行是否和board[x][y]重复
            for i in range(9):
                if y != i and board[x][i] == board[x][y]:
                    return False

            # 检查纵行是否和board[x][y]重复
            for i in range(9):
                if x != i and board[i][y] == board[x][y]:
                    return False

            # 检查3*3的小矩阵是否和board[x][y]重复
            for i in range(3):
                for j in range(3):
                    # x/3 找到是第几个3*3的矩阵
                    if x/3*3+i!=x and y/3*3+j!=y and board[x/3*3+i][y/3*3+j] == board[x][y]:
                        return False
            return True

    
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if check(i,j,board) == False:
                    return False
        return True


