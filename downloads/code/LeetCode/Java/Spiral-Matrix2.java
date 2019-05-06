public class Solution {
    public int[][] generateMatrix(int n) {
        int[][] ret = new int[n][n];
        int i=0; int j=0;

        int di=0; int dj=1;
        for(int k=0;k<n*n;k++){
            ret[i][j] = k+1;
            if(i+di <0 || j+dj < 0 || ret[(i+di)%n][(j+dj)%n]!=0){
                int tmp = di;
                di = dj;
                dj = -tmp;
            }
            i += di;
            j += dj;
        
        }
        return ret;
    }
}
