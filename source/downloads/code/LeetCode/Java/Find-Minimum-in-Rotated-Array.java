public class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length-1;
        if (nums.length==1)
	    return nums[0];
        while (l<r){
            int m = l+(r-l)/2;
            if (m > 0 && nums[m]<nums[m-1])
                return nums[m];
            if (nums[l]<=nums[m] && nums[m] > nums[r])
                l = m+1;
            else
                r = m-1;;
        }
        return nums[l];        
    }
}
