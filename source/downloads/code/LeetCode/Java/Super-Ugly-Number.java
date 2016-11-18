import java.util.Arrays;

public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        int[] ugly = new int[n];
        //
        int[] idx = new int[primes.length];
        int[] val = new int[primes.length];

        Arrays.fill(val, 1);

        // next ugly value
        int next = 1;
        for(int i=0;i<n;i++){
            ugly[i] = next;

            next = Integer.MAX_VALUE;
            for( int j=0; j<primes.length;j++){
                if(val[j] == ugly[i])
                    val[j] = ugly[idx[j]++] * primes[j];
                next = Math.min(next, val[j]);
            }
        }

     return ugly[n-1]; 

    }
    public static void main(String arg[]){
    
        sol = Solution();
        sol.nthSuperUglyNumber(14, [2,7,13,19]);
    
    }
}
