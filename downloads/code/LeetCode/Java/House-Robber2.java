public class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(nums.length==1)
           return nums[0];
        return Math.max(rob_helper(nums, 0, n-2), rob_helper(nums, 1, n-1)); 
    }

    public int rob_helper(int[] nums, int lo, int hi){
        int include = 0;
        int exclude = 0;
        for(int j=lo; j<=hi; j++){
            int i = include; int e = exclude;
            include = nums[j]+e;
            // 为什么不是exclude = i: [1,3,1,3,100]
            exclude = Math.max(e,i);
        }
        return Math.max(include,exclude);
    }
}
