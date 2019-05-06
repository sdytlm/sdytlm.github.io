public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int sum = 0;
        int start = 0;
        int end = 0;
        int ret = Integer.MAX_VALUE;
        while(end<nums.length){
            // 找到一个序列，使sum>=s
            while(end<nums.length && sum < s){
                sum += nums[end];
                end++;
            }
            // 没有解了
            if(sum < s) break;

            // 寻找该序列的start
            while(start<end && sum>=s){
                sum -= nums[start];
                start++;
            }

            ret = Math.min(ret,end-start+1);
        }
        
        return ret==Integer.MAX_VALUE?0:ret;
    }
}
