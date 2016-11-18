public class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        Map<Integer, Integer> map = new HashMap<>();
   
        for(int a=0; a<A.length; a++){
            for(int b=0; b<B.length; b++){
                int sum = A[a] + B[b];    
                map.put(sum, map.getOrDefault(sum,0)+1);
            }
        }    
        int ret = 0;
        for(int c=0; c<C.length; c++){
            for(int d=0; d<D.length; d++){
                int sum = C[c] + D[d];
                ret += map.getOrDefault(-sum, 0);
            } 
        }
        return ret;
    }
}
