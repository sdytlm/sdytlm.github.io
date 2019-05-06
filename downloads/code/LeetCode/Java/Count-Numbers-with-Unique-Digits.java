public class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        int[] dp = new int[11];
        if(n==0) return 1;
        if (n >10)
            return 0;
        dp[1] = 10;
        dp[2] = 9*9;
        for(int i = 3; i<=10; i++){
            dp[i] = dp[i-1]*(11-i);
        }
        // Get f[1]+f[2]+...f[n]
        int ret = 0;
        for (int i=0;i<=n;i++)
            ret += dp[i];
        return ret;
    }
}
