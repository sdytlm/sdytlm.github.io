public class Solution {
    public void nextPermutation(int[] nums) {
        // 找到递减序列的前一个
        if (nums.length < 2)
            return;
        int k = nums.length-2;
        while (k>=0 && nums[k] >= nums[k+1])
            k-=1;

        // 5 4 3 2 1
        if (k < 0){
            Arrays.sort(nums);
	    return ;
	}
        // 找到k后面最小值
        int l = nums.length-1;
        while (l>k && nums[l]<=nums[k])
            l -=1;

        // swap a[l],a[k]
        int tmp = nums[k];
        nums[k] = nums[l];
        nums[l] = tmp;

        // reverse array after k
        reverse(nums,k+1);
        
    }
    public void reverse(int[] nums, int index){
        int r = nums.length-1;
        int l = index;
        while (l<r){
            int tmp = nums[l];
            nums[l] = nums[r];
            nums[r] = tmp;
            l += 1;
            r -= 1;
        }
    
    }
}
