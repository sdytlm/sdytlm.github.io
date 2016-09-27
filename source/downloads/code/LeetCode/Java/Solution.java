public class Solution {
    public static void main(String[] args){
       Solution sol = new Solution();
       int[] nums = {5,1,3};
       sol.search(nums, 3);
        
    }

    public boolean search(int[] nums, int target) {
            int n = nums.length;
            int l = 0;
            int r = n-1;
            while(l<=r){

                while(l<r && nums[l]==nums[l+1]) l++;
                while(l<r && nums[r]==nums[r-1]) r--;

                int m = l+(r-l)/2;
                if (nums[m] == target)
                    return true;
                    
                if(nums[m]>=nums[l]){
                    if(target >= nums[l] && target < nums[m])
                        r = m-1;
                    else
                        l = m+1;
                }
                else{
                    if(target <= nums[r] && target > nums[l])
                        l = m+1;
                    else
                        r = m-1;
                }
            }
        return false;            
    }
}
