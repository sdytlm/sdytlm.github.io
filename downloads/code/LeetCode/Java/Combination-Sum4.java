public class Solution {
    public int combinationSum4(int[] nums, int target) {
        int n = nums.length;
        if (n==0) return 0;
        int[] dp = new int[target+1];
        Arrays.sort(nums);
        for(int i=0; i<dp.length;i++){
            for(int num : nums){
                if(num > i)
                    break;
                if(num == i)
                    dp[i]++;
                else if(num < i)
                    dp[i] += dp[i-num];
                
            }
        
        }
        return dp[target];
    }
}
