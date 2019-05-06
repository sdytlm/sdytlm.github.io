public class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        if(n==0) return false;
        int index_true = n-1;
        for(int i=n-2; i>=0; i--){
            if(i+nums[i] >= index_true) 
                index_true = i;
        
        }
        return index_true==0;
                
    }
}
