public class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ret = new int[n];
        //累乘nums[i]左面的
        ret[0] = 1;
        for (int i=1;i<n;i++){
            ret[i] = nums[i-1]*ret[i-1]; 
        }
        
        // 类成nums[i]右边的
        int right = 1;
        for (int i=n-1;i>=0;i--){
            ret[i] *= right;
            right *= nums[i];
        }
        return ret;
    }
}
