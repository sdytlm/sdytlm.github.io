  class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int col = matrix[0].length;
        int row = matrix.length;

        int i = 0;
        int j = col-1;

        while(i<row && j>=0){
            if(target == matrix[i][j])
                return true;
            if(target>matrix[i][j]){
                i++;
            }
            else
                j--;
        }
        return false;
    }
}
