public class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        char[] w = word.toCharArray();
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(dfs(board,i,j,w,0))
                    return true;
            }
        }
        return false;
    }

    public boolean dfs(char[][] board, int row, int col, char[] word, int index){
        if(index==word.length) return true;
        if(row < 0 || col < 0 || row == board.length || col == board[0].length) return false;
        if(word[index] != board[row][col]) return false;
        board[row][col] ^= 256;
        boolean ret = dfs(board,row,col+1, word, index+1) || 
                      dfs(board,row+1,col, word, index+1) ||
                      dfs(board,row,col-1, word, index+1) ||
                      dfs(board,row-1,col, word, index+1);
        board[row][col] ^= 256;
        return ret;
    }
}





