public class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        if (n==0)
            return 0;
        int maxSoFar = nums[0];
        int maxEnding = nums[0];
        for (int i=1;i<n;i++){
            maxEnding = Math.max(nums[i],nums[i]+maxEnding);
            maxSoFar = Math.max(maxSoFar, maxEnding); 
        }        
        return maxSoFar;
    }
}
