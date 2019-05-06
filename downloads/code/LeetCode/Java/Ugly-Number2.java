public class Solution {
    public int nthUglyNumber(int n) {
        int[] dp = new int[n+1];
        dp[1] = 1;
        int p1 = 1;
        int p2 = 1;
        int p3 = 1;
        for(int i=2; i<=n; i++){
            dp[i] = Math.min(2*dp[p1], Math.min(3*dp[p2], 5*dp[p3]));
            if(dp[i]==2*dp[p1]) p1++;
            if(dp[i]==3*dp[p2]) p2++;
            if(dp[i]==5*dp[p3]) p3++;
        }
        return dp[n];
    }
}
