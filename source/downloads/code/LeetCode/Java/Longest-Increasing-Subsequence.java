public class Solution {
    public int lengthOfLIS(int[] nums) {
        if(nums.length==0) return 0;
        int []dp = new int[nums.length];
        // dp的实际长度
        int len = 0;
        for(int num: nums){
            // 在dp中找num
            int i = Arrays.binarySearch(dp, 0, len, num);
            if(i<0) i = -(i+1);
            // 更新dp
            dp[i] = num;
            if(i==len) len++;
        }
        return len;
    }
}
