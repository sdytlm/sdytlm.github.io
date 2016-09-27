public class Solution {
    public int numTrees(int n) {
        int[] dp = new int[n+1];
        if (n<2)
            return 1;
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;

        for (int i=3;i<=n;i++){
            int sum = 0;
            for(int j=0;j<i;j++){
                sum += dp[j]*dp[i-j-1];
            }
            dp[i] = sum;
        }
        return dp[n];
    }
}
