public class Solution {
    public int missingNumber(int[] nums) {
        int xor = 0;
        int i;
        for (i=0;i<nums.length; i++){
            xor = xor ^ i;
            xor = xor ^ nums[i];
        }
        return xor ^ i;
    }
}
