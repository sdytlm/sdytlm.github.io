public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ret = new LinkedList<Integer>();
        if (matrix.length == 0) return ret;
        
        int l = 0;
        int r = matrix[0].length-1;
        int u = 0;
        int d = matrix.length-1;
        
        //　方向
        int[] direction = {0,1,2,3};
        int i = 0;

        while ((l<=r) && (u<=d)){
            if (direction[i%4] == 0){
                for (int j=l; j<=r;j++)
                    ret.add(matrix[u][j]);
                u += 1;
                
            }
            else if (direction[i%4] == 1){
                for (int j=u;j<=d;j++)
                    ret.add(matrix[j][r]);
                r -= 1;
            } 
            else if (direction[i%4] == 2){
                for (int j=r; j>=l;j--)
                    ret.add(matrix[d][j]);
                d -= 1;
                
            } 
            else{
                for (int j=d; j>=u;j--)
                    ret.add(matrix[j][l]);
                l += 1;
            }
            i += 1;
        }
        return ret;
    }
}
