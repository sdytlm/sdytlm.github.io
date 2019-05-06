public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        
        int start = matrix[0][0];
        int end = matrix[n-1][n-1];
        while(start <= end){
            int mid = start+(end-start)/2;
            int cnt = countLower(matrix, mid);
            if (cnt < k)
                start = mid+1;
            else
                end = mid-1;
        }
        return start;
    }

    public int countLower(int[][] matrix, int target){
        int n = matrix.length;
        // 横纵坐标
        int i = n-1;
        int j = 0;
        int ret = 0;

        while(i>=0 && j<n){
            if(matrix[i][j] <= target){
                ret += i+1;
                j++;
            }
            else
                i--;
        }
        return ret;
    }
}
