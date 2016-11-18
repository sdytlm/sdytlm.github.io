public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int ret = 0;
        int cur = 0;
        if (A.length<3) return 0;
        for(int i=2;i<A.length;i++){
            if(A[i]-A[i-1] == A[i-1]-A[i-2]){
                cur ++;
                ret += cur;
            }
            else
                cur = 0;
        
        }
        return ret;        
    }
}
