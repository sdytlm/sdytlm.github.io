public class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        if(n==0)
            return 0;
        int[] pos = new int[n];    
        int[] neg = new int[n];
        pos[0] = nums[0];
        neg[0] = nums[0];

        for(int i=1;i<n;i++){
            pos[i] = Math.max(Math.max(pos[i-1]*nums[i], neg[i-1]*nums[i]), nums[i]);
            neg[i] = Math.min(Math.min(pos[i-1]*nums[i], neg[i-1]*nums[i]), nums[i]);
        }
        int ret = pos[0];
        for(int i=0;i<n;i++){
            if(ret<pos[i])
                ret = pos[i];
        }
        return ret;
    }
}
