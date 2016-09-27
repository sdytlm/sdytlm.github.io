public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int min = Integer.MAX_VALUE;
        int n = nums.length;
        int ret = 0;
        for (int i=0;i<n;i++){
            int s = i+1;
            int e = n-1;
            while(s<e){
                int sum = nums[i]+nums[s]+nums[e];
                if (Math.abs(sum-target) < min)
                {
                    min = Math.abs(sum-target);
                    ret = sum;
                }

                if (sum==target){
                    return sum;
                }
                else if (sum < target)
                    s ++;
                else
                    e --;
            }
        }
        return ret;
    }
}
