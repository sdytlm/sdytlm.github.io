public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        for(int i=1; i<=n; i++)
            dp[i] = Integer.MAX_VALUE;
        // init 所有完全平方数
        for(int i=1; i<=n; i++){
            if(i*i<=n) 
                dp[i*i]=1;
        }
        
     
        for(int i=1;i<=n;i++){
            for(int j=1; i+j*j<=n; j++){
                dp[i+j*j] = Math.min(dp[i]+1,dp[i+j*j]);
            }
        }
        return dp[n];
    }
}

