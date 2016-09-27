public class Solution {
    public boolean isValidSudoku(char[][] board) {
        int row = board.length;
        int col = board[0].length;

        for(int i=0;i<row;i++){
            for (int j=0;j<col;j++){
                if (board[i][j]=='.') continue;
            
                // 行
                int k=0;
                while (k<9){
                    if(j!=k && board[i][k] == board[i][j])
                        return false;
                    k+=1;    
                }
            
                // 列
                k = 0;
                while(k<9){
                    if (i!=k && board[k][j] == board[i][j])
                        return false;
                    k+=1;
                }

                // ３×３
                for (int m=0;m<3;m++){
                    for (int n=0;n<3;n++){
                        if (i/3*3+m !=i && j/3*3+n != j && board[i][j] == board[i/3*3+m][j/3*3+n])
                            return false;
                    }
                }
            }
        }
        return true;       
    }
}
