public class Solution {
    public int cnt(int[][] board, int row, int col) {
        int[] dx = {0,0,-1,-1,-1,1,1,1};
        int[] dy = {1,-1,0,-1,1,-1,0,1};

        int m = board.length;
        int n = board[0].length;

        int ret = 0;
        for(int i=0;i<8;i++){
            int x = dx[i]+row;
            int y = dy[i]+col;
            if(x<0 || y<0 || x>=m || y>=n) continue;
            if(board[x][y]==1 || board[x][y]==2) ret++;

        }
        return ret;

    }
    public void gameOfLife(int[][]board){
        int m=board.length;
        int n=board[0].length;
        if(m==0 || n==0)
            return ;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int count = cnt(board,i,j);
                if(board[i][j] != 0){
                    if(count!=2 && count!=3)
                        board[i][j] = 2;
                }
                else{
                    if(count==3)
                        board[i][j] = 3;
                
                }
            }
        }
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                board[i][j] &= 1;

    }
}
