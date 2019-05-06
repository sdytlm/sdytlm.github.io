public class Solution {
    public void wiggleSort(int[] nums) {
        // 找中位数
        // Use quick sort or heap to implement the following func
        int mid = findKthLargest(nums, (nums.length+1)/2);
        int n = nums.length;
        int left = 0;
        int idx = 0;
        int right = n-1;

        while(idx <= right){
            if(nums[newIndex(idx,n)] < mid)
                swap(nums, newIndex(left++, n), newIndex(idx++, n));
            else if (nums[newIndex(idx,n)] > mid)
                swap(nums, newIndex(idx,n), newIndex(right--, n));
            else
                idx++;
        
        }

    }
    // index rewiring
    private int newIndex(int index, int n){
        return (1+2*index)%(n|1);
    }
}
