public class Solution {
    public int findPeakElement(int[] nums) {
        int n = nums.length;
        return bs(nums,0,n-1);   
    }

    public int bs(int[] nums, int start, int end){
        if(start==end)
            return start;
        int mid1 = start+(end-start)/2;
        int mid2 = mid1+1;
        if(nums[mid1]>nums[mid2])
            return bs(nums, start,mid1);
        else
            return bs(nums, mid2,end);
    }
}

public class Solution {
    public int findPeakElement(int[] nums){
        int end = nums.length-1;
        int start = 0;
        while(start<end){
            int mid1 = start+(end-start)/2;
            int mid2 = mid1+1;
            if(nums[mid1]>nums[mid2])
                end = mid1;
            else
                start = mid2;
        
        }
        return start;
    }

}
