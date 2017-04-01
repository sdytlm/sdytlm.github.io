public class NumMatrix {
    int row, col;
    int[][] sums;

    public NumMatrix(int[][] matrix) {
	this.row = matrix.length;
	this.col = this.row>0? matrix[0].length : 0;
	this.sums = new int[this.row+1][this.col+1];
	for(int i=1; i<=this.row; i++){
	    for(int j=1; j<=this.col;j++)
		this.sums[i][j] = this.sums[i-1][j]+this.sums[i][j-1]-this.sums[i-1][j-1]+matrix[i-1][j-1];
	}
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
	return this.sums[row2+1][col2+1] - this.sums[row2+1][col1] - this.sums[row1][col2+1] + this.sums[row1][col1];
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
