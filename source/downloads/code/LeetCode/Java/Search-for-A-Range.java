public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        int[] ret = {-1, -1};
        if(n==0) return ret;
        int l = 0;
        int r = n-1;

        while(l<=r){
            int mid = l+(r-l)/2;
            if(nums[mid]<target)
                l = mid+1;
            else
                r = mid-1;
        }
        // 有可能找不到
        if(l>=n || nums[l]!=target) return ret;
        ret[0] = l;

        l=0;
        r = n-1;
        while(l<=r){
            int mid = l+(r-l)/2;
            if(nums[mid]<=target)
                l = mid+1;
            else
                r = mid-1;
        }
        ret[1] = r;
        return ret;
    }
}
