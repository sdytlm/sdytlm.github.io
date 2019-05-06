public class Solution {
    public int getMoneyAmount(int n) {
        if(n==1) return 0;
        int [][]dp = new int[n+1][n+1];
        for(int jminusi = 1; jminusi < n; jminusi ++){
            for(int i=1; i+jminusi <=n; i++){
                int j=i+jminusi;
                dp[i][j] = Integer.MAX_VALUE;
                for(int k=i;k<j;k++)
                    dp[i][j] = Math.min(dp[i][j], k+Math.max(dp[i][k-1],dp[k+1][j]));
            
            
            }
        
        
        }
        return dp[1][n];
    }
}
