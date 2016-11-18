public class Solution {
    int[] nums;
    Random random;
    public Solution(int[] nums) {
        this.nums = nums;
        random = new Random();
    }
    
    public int pick(int target) {
        int count = 0;
        int ret = 0;
        for(int i = 0; i<this.nums.length; i++){
            if(this.nums[i] != target) continue;
            if(random.nextInt(++count) == 0)
                ret = i;
        }
        return ret;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
