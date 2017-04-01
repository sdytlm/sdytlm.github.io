public class Solution {
    public void solve(char[][] board) {
        int i,j;
	int row = board.length;
	if(row==0) return;
	int col = board[0].length;
	for(i=0;i<row;i++){
	    // check first and last col
	    check(board,i,0,row,col);
	    check(board,i,col-1,row,col);
	}

	for(j=0;j<col;j++){
	    // check first and last row
	    check(board,0,j,row,col);
	    check(board,row-1,j,row,col);
	}

	// change all "O" to "x"
	for(i=0;i<row;i++)
	    for(j=0;j<col;j++)
		if(board[i][j]=='O') board[i][j] = 'X';

	// change "1" to "O"
	for(i=0;i<row;i++)
	    for(j=0;j<col;j++)
		if(board[i][j]=='1') board[i][j] = 'O';
	
    }

    public void check(char[][] board, int i, int j, int row, int col){

	if(board[i][j] == 'O'){
	    board[i][j] = '1';
	    if (i>1)	    
	        check(board,i-1,j,row,col);
	    if (j>1)
	        check(board,i,j-1,row,col);
	    if (i+1 < row)
	        check(board,i+1,j,row,col);
	    if (j+1 < col)
	        check(board,i,j+1,row,col);
	}
    }
}
